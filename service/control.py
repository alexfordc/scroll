__author__ = 'ict'

import threading
import os

import service.configure
from service.helper import package
from service.helper import send_file
from service.helper import receive_file


def get_vardict():
    var_dict = {}
    for file in os.listdir(service.configure.save_path):
        file_sep = file.split(".")
        var_dict[file_sep[0]] = file_sep[1]
    return var_dict


class ServerThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connect = connection
        self.address = address

    def run(self):
        self.connect.send(package("start"))
        if service.configure.save_path[-1] != os.path.sep:
            service.configure.save_path += os.path.sep
        while True:
            cmd = self.connect.recv(1024).decode()
            if cmd == "save":
                self.connect.send(package("name"))
                data_name = self.connect.recv(256).decode()
                self.connect.send(package("type"))
                data_type = self.connect.recv(256).decode()
                receive_file(self.connect, service.configure.save_path + data_name + "." + data_type)
            elif cmd == "load":
                self.connect.send(package("name"))
                data_name = self.connect.recv(256).decode()
                vs = get_vardict()
                filename = ""
                if data_name in vs:
                    filename = data_name + "." + vs[data_name]
                self.connect.send(package(filename))
                send_file(self.connect, service.configure.save_path + filename)