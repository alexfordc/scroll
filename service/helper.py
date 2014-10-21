__author__ = 'ict'

import os

import service.configure


def package(text):
    return text.encode(encoding='utf-8', errors='strict')


def send_file(sk, filename):
    while not sk.recv(256).decode() == "size":
        pass
    sk.send(package(str(os.path.getsize(filename))))
    while not sk.recv(256).decode() == "data":
        pass
    fp = open(filename, "rb")
    while True:
        data = fp.read(1024 * 1024)
        if not data:
            break
        sk.send(data)
    fp.close()


def receive_file(sk, filename):
    sk.send(package("size"))
    data_size = int(sk.recv(256).decode())
    sk.send(package("data"))
    fp = open(filename, "wb")
    while data_size:
        if data_size > service.configure.receive_buffer:
            data = sk.recv(service.configure.receive_buffer)
        else:
            data = sk.recv(data_size)
        fp.write(data)
        data_size -= len(data)
    fp.close()