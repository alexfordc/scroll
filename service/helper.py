__author__ = 'ict'

import service.configure


def package(text):
    return text.encode(encoding='utf-8', errors='strict')


def wait_cmd(sk, cmd):
    while not sk.recv(len(cmd)).decode() == cmd:
        pass


def response(sk, cmd, data):
    wait_cmd(sk, cmd)
    sk.send(package(str(data)))


def request(sk, cmd):
    sk.send(package(cmd))
    return sk.recv(service.configure.msg_buffer).decode()