__author__ = 'ict'

import socket
import time

import service.configure
import service.control
import service.object_pool


server_pool = []


if __name__ == "__main__":
    print("Create Object Pool...")
    op = service.object_pool.ObjectPool(service.configure.object_pool_dump, service.configure.save_path)
    print("Create Socket...")
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((service.configure.ip, service.configure.port))
    sk.listen(service.configure.max_connection)
    print("Listening...")
    while True:
        connection, address = sk.accept()
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("%s [New connection] %s:%s" % (time_str, address[0], address[1]))
        server_pool.append(service.control.ServerThread(connection, address, op))
        server_pool[-1].start()