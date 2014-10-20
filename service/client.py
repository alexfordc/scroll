__author__ = 'ict'

import socket
import os

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
        while not self.sk.recv(256).decode() == "name":
            pass
        self.sk.send(package(name))
        while not self.sk.recv(256).decode() == "type":
            pass
        self.sk.send(package(data_type))
        while not self.sk.recv(256).decode() == "data":
            pass
        fp = open(filename, "rb")
        while True:
            data = fp.read(1024 * 1024)
            if not data:
                break
            self.sk.send(data)
        fp.close()
        os.remove(filename)

    def load(self, name):
        self.sk.send(package("load"))
        while not self.sk.recv(256).decode() == "name":
            pass
        self.sk.send(package(name))
        filename = self.sk.recv(256).decode()
        self.sk.send(package("data"))
        fp = open(filename, "wb")
        while True:
            data = self.sk.recv(1024 * 1024)
            fp.write(data)
            if len(data) < 1024 * 1024:
                break
        fp.close()
        var = DAL.file.load(filename)
        os.remove(filename)
        return var