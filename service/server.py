__author__ = 'ict'

import socket

import service.configure
import service.control
import service.object_pool


server_pool = []


if __name__ == "__main__":
    op = service.object_pool.ObjectPool(service.configure.object_pool_dump, service.configure.save_path)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((service.configure.ip, service.configure.port))
    sk.listen(service.configure.max_connection)
    while True:
        connection, address = sk.accept()
        server_pool.append(service.control.ServerThread(connection, address, op))
        server_pool[-1].start()