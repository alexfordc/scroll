__author__ = 'ict'

import threading
import os

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
        self.connect.send(package("start"))
        if service.configure.save_path[-1] != os.path.sep:
            service.configure.save_path += os.path.sep
        while True:
            cmd = self.connect.recv(service.configure.cmd_buffer).decode()
            if len(cmd) != 0:
                print("[%s:%s] " % (self.address[0], self.address[1]) + cmd)
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
                obj_dict = self.object_pool.copy_object()
                self.connect.send(package(str(obj_dict)))