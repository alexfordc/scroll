__author__ = 'ict'

import socket

import DAL.file


def package(text):
    return text.encode(encoding='utf-8', errors='strict')


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.connect((self.ip, self.port))

    def save(self, var, name):
        data_type = str(type(var))[8:-2]
        filename = name + "." + data_type
        DAL.file.save(var, filename)
        self.sk.send(package("save"))
        while not self.sk.recv(1024).decode() == "name":
            pass
        self.sk.send(package(name))
        while not self.sk.recv(1024).decode() == "type":
            pass
        self.sk.send(package(data_type))
        while not self.sk.recv(1024).decode() == "data":
            pass
        fp = open(filename, "rb")
        while True:
            data = fp.read(1024 * 1024)
            if not data:
                break
            self.sk.send(data)
        fp.close()