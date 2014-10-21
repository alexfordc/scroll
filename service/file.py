__author__ = 'ict'

import os

import service.configure
from service.helper import response
from service.helper import package


def send_file(sk, filename):
    response(sk, "size", os.path.getsize(filename))
    while not sk.recv(service.configure.msg_buffer).decode() == "data":
        pass
    fp = open(filename, "rb")
    while True:
        data = fp.read(service.configure.file_buffer)
        if not data:
            break
        sk.send(data)
    fp.close()


def receive_file(sk, filename):
    sk.send(package("size"))
    data_size = int(sk.recv(service.configure.msg_buffer).decode())
    sk.send(package("data"))
    fp = open(filename, "wb")
    while data_size:
        if data_size > service.configure.file_buffer:
            data = sk.recv(service.configure.file_buffer)
        else:
            data = sk.recv(data_size)
        fp.write(data)
        data_size -= len(data)
    fp.close()