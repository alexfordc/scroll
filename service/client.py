__author__ = 'ict'

import socket
import os

import DAL.file
import service.configure
import service.object_pool
from service.helper import package
from service.helper import response
from service.file import send_file
from service.file import receive_file


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.connect((self.ip, self.port))
        msg = self.sk.recv(256).decode()
        if msg != "start":
            raise Exception("Can not connect")

    def close(self):
        self.sk.close()

    def save(self, var, name):
        self.sk.send(package("save"))
        data_type = str(type(var))[8:-2]
        filename = name + "." + data_type
        DAL.file.save(var, filename)
        response(self.sk, "name", name)
        response(self.sk, "type", data_type)
        state = self.sk.recv(service.configure.msg_buffer).decode()
        if state != service.object_pool.success_msg:
            return state
        send_file(self.sk, filename)
        os.remove(filename)
        return state

    def load(self, name):
        self.sk.send(package("load"))
        response(self.sk, "name", name)
        filename = self.sk.recv(service.configure.msg_buffer).decode()
        if filename == service.configure.no_such_object:
            return None
        state = self.sk.recv(service.configure.msg_buffer).decode()
        if state != service.object_pool.success_msg:
            return None
        receive_file(self.sk, filename)
        var = DAL.file.load(filename)
        os.remove(filename)
        return var

    def remove(self, name):
        self.sk.send(package("remove"))
        response(self.sk, "name", name)
        rst = self.sk.recv(service.configure.msg_buffer).decode()
        if rst == service.object_pool.success_msg:
            return name + " has been removed"
        else:
            return rst

    def list(self):
        self.sk.send(package("list"))
        rst = self.sk.recv(service.configure.msg_buffer).decode()
        return eval(rst)