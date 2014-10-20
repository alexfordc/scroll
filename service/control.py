__author__ = 'ict'

import threading


def package(text):
    return text.encode(encoding='utf-8', errors='strict')


class ServerThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connect = connection
        self.address = address

    def run(self):
        self.connect.send(package("start"))
        while True:
            cmd = self.connect.recv(1024).decode()
            if cmd == "save":
                self.connect.send(package("name"))
                data_name = self.connect.recv(256).decode()
                self.connect.send(package("type"))
                data_type = self.connect.recv(256).decode()
                self.connect.send(package("data"))
                fp = open(data_name + "." + data_type, "wb")
                while True:
                    data = self.connect.recv(1024 * 1024)
                    if data == "EOF":
                        break
                    fp.write(data)
                fp.close()
            elif cmd == "load":
                self.connect.send(package("name"))
                data_name = self.connect.recv(256)
                self.connect.send(package("type"))
                data_type = self.connect.recv(256)
                fp = open(data_name + "." + data_type, "wb")
                data = fp.read()
                fp.close()
                self.connect.send(data)