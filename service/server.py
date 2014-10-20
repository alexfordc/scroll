__author__ = 'ict'

import socket
import service.configure
import service.control


server_pool = []


if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((service.configure.ip, service.configure.port))
    sk.listen(service.configure.max_connection)
    while True:
        connection, address = sk.accept()
        server_pool.append(service.control.ServerThread(connection, address))
        server_pool[-1].start()