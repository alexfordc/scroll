__author__ = 'ict'

import socket
import os

import DAL.file
from service.helper import package
from service.helper import send_file
from service.helper import receive_file


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.connect((self.ip, self.port))
        msg = self.sk.recv(256).decode()
        if msg != "start":
            raise Exception("Can not connect")

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
        send_file(self.sk, filename)
        os.remove(filename)

    def load(self, name):
        self.sk.send(package("load"))
        while not self.sk.recv(256).decode() == "name":
            pass
        self.sk.send(package(name))
        filename = self.sk.recv(256).decode()
        receive_file(self.sk, filename)
        var = DAL.file.load(filename)
        os.remove(filename)
        return var