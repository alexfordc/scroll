__author__ = 'ict'

import threading
import os
import time

import calculate.feature.core
import calculate.helper.PCA
import service.configure
import service.object_pool
from service.helper import package
from service.helper import request
from service.file import send_file
from service.file import receive_file


class ServerThread(threading.Thread):
    def __init__(self, connection, address, object_pool):
        threading.Thread.__init__(self)
        self.connect = connection
        self.address = address
        self.object_pool = object_pool

    def run(self):
        try:
            self.connect.send(package("start"))
        except ConnectionError:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print("%s [%s:%s] Abnormal connection." % (time_str, self.address[0], self.address[1]))
            self.connect.close()
            return
        if service.configure.save_path[-1] != os.path.sep:
            service.configure.save_path += os.path.sep
        if service.configure.exec_path[-1] != os.path.sep:
            service.configure.exec_path += os.path.sep
        while True:
            try:
                cmd = self.connect.recv(service.configure.cmd_buffer).decode()
                if len(cmd) != 0:
                    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    print("%s [%s:%s] " % (time_str, self.address[0], self.address[1]) + cmd)
                if cmd == "close":
                    self.connect.close()
                    break
                if cmd == "save":
                    data_name = request(self.connect, "name")
                    data_type = request(self.connect, "type")
                    filename = service.configure.save_path + data_name + "." + data_type
                    rst = self.object_pool.add_object(data_name, data_type, 0)
                    if rst != service.object_pool.success_msg:
                        self.connect.send(package(rst))
                        continue
                    rst = self.object_pool.lock_object(data_name)
                    if rst != service.object_pool.success_msg:
                        self.connect.send(package(rst))
                        continue
                    self.connect.send(package(service.object_pool.success_msg))
                    receive_file(self.connect, filename)
                    self.object_pool.unlock_object(data_name)
                    self.object_pool.update_object(data_name)
                elif cmd == "load":
                    data_name = request(self.connect, "name")
                    filename = self.object_pool.filename_object(data_name)
                    if filename is None:
                        self.connect.send(package(service.configure.no_such_object))
                        continue
                    else:
                        self.connect.send(package(filename))
                    rst = self.object_pool.lock_object(data_name)
                    if rst != service.object_pool.success_msg:
                        self.connect.send(package(rst))
                        continue
                    self.connect.send(package(service.object_pool.success_msg))
                    send_file(self.connect, service.configure.save_path + filename)
                    self.object_pool.unlock_object(data_name)
                elif cmd == "remove":
                    data_name = request(self.connect, "name")
                    rst = self.object_pool.del_object(data_name)
                    self.connect.send(package(rst))
                elif cmd == "list":
                    obj_dict = self.object_pool.copy_entry_object()
                    self.connect.send(package(str(obj_dict)))
                elif cmd == "rename":
                    data_name = request(self.connect, "name")
                    rename_name = request(self.connect, "rename")
                    rst = self.object_pool.rename_object(data_name, rename_name)
                    self.connect.send(package(rst))
                elif cmd == "clone":
                    data_name = request(self.connect, "name")
                    clone_name = request(self.connect, "clonename")
                    rst = self.object_pool.clone_object(data_name, clone_name)
                    self.connect.send(package(rst))
                elif cmd == "execute":
                    filename = request(self.connect, "filename")
                    filename = service.configure.exec_path + filename
                    count = 0
                    real_filename = filename
                    while os.path.exists(filename):
                        index = filename.rfind(".")
                        real_filename = filename[: index] + str(count) + filename[index:]
                        count += 1
                    filename = real_filename
                    receive_file(self.connect, filename)
                    outfile = filename + ".out"
                    with open(filename, "r") as fp:
                        data = fp.read()
                        data.replace("\r\n", "\n")
                        head = "import sys\nfp = open(r\"%s\", \"w\")\nsys.stdout = fp\nsys.stderr = fp\n" % outfile
                        data = head + data
                    with open(filename, "w") as fp:
                        fp.write(data)
                    os.system(service.configure.python + " " + filename)
                    self.connect.send(package("output"))
                    send_file(self.connect, outfile)
                elif cmd == "file":
                    files = os.listdir(service.configure.exec_path)
                    file_info = []
                    for file in files:
                        if file[-3:] != ".py":
                            continue
                        file_info.append((file, os.path.getctime(service.configure.exec_path + file)))
                    self.connect.send(package(str(file_info)))
                elif cmd == "delete":
                    file = request(self.connect, "file")
                    if file == "*":
                        files = os.listdir(service.configure.exec_path)
                        for file in files:
                            os.remove(service.configure.exec_path + file)
                    else:
                        if not os.path.exists(service.configure.exec_path + file):
                            self.connect.send(package("No such python file: " + file))
                        os.remove(service.configure.exec_path + file)
                        if os.path.exists(service.configure.exec_path + file + ".out"):
                            os.remove(service.configure.exec_path + file + ".out")
                    self.connect.send(package(service.object_pool.success_msg))
                elif cmd == "feature":
                    data_name = request(self.connect, "name")
                    rst_name = request(self.connect, "rstname")
                    mtd = request(self.connect, "mtd")
                    option = eval(request(self.connect, "option"))
                    main = eval(request(self.connect, "main"))
                    unpack = eval(request(self.connect, "unpack"))
                    if not self.object_pool.avilable_object(data_name):
                        self.connect.send(package(service.object_pool.unavilable_msg + data_name))
                        continue
                    if self.object_pool.have_object(rst_name):
                        self.connect.send(package(service.object_pool.exist_msg + rst_name))
                        continue
                    self.object_pool.add_object(rst_name, "dict", 0)
                    rst = self.object_pool.lock_object(rst_name)
                    if rst != service.object_pool.success_msg:
                        self.connect.send(package(rst))
                        continue
                    data_dict = self.object_pool.get_object(data_name)
                    try:
                        for key, value in data_dict.items():
                            data_dict[key] = calculate.feature.core.method(mtd, value, option, main, unpack)
                        self.object_pool.save_object(rst_name, data_dict)
                        self.object_pool.update_object(rst_name)
                        self.object_pool.unlock_object(rst_name)
                    except Exception as e:
                        self.object_pool.unlock_object(rst_name)
                        self.connect.send(package(str(e)))
                        continue
                    self.connect.send(package(service.object_pool.success_msg))
                elif cmd == "pca":
                    data_name = request(self.connect, "name")
                    rst_name = request(self.connect, "rstname")
                    n = int(request(self.connect, "n"))
                    if not self.object_pool.avilable_object(data_name):
                        self.connect.send(package(service.object_pool.noexist_msg + data_name))
                        continue
                    if self.object_pool.have_object(rst_name):
                        self.connect.send(package(service.object_pool.exist_msg + rst_name))
                        continue
                    self.object_pool.add_object(rst_name, "dict", 0)
                    rst = self.object_pool.lock_object(rst_name)
                    if rst != service.object_pool.success_msg:
                        self.connect.send(package(rst))
                        continue
                    data_dict = self.object_pool.get_object(data_name)
                    try:
                        data_dict = calculate.helper.PCA.pca(data_dict, n)
                        self.object_pool.save_object(rst_name, data_dict)
                        self.object_pool.update_object(rst_name)
                        self.object_pool.unlock_object(rst_name)
                    except Exception as e:
                        self.object_pool.unlock_object(rst_name)
                        self.connect.send(package(str(e)))
                        continue
                    self.connect.send(package(service.object_pool.success_msg))
            except Exception as e:
                time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                print("%s [%s:%s] %s" % (time_str, self.address[0], self.address[1], str(e)))
                self.connect.close()
                break
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("%s [Close connection] %s:%s" % (time_str, self.address[0], self.address[1]))