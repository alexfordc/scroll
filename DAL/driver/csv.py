__author__ = 'ict'

import os


class CSV:
    def __init__(self, file=None):
        self.data = []
        self.file = file
        self.tag = None
        self.loaded = False

    def load(self, file=None):
        if file is None:
            file = self.file
        if file is None:
            raise Exception("Need input file name")
        if not os.path.isfile(file):
            raise FileNotFoundError("No such file: " + file)
        self.tag = file.lower().replace(".csv", "")
        with open(file, "r") as csv_fp:
            buff = csv_fp.read()
        self.data = []
        if "\r\n" in buff:
            buff_list = buff.split("\r\n")
        else:
            buff_list = buff.split("\n")
        for item in buff_list:
            if len(item) == 0:
                continue
            item_list = item.split(",")
            tmp_list = []
            for each in item_list:
                if len(each) != 0:
                    if each[0] == "\"" and each[-1] == "\'":
                        tmp_list.append(each[1:-1])
                    else:
                        tmp_list.append(each)
            self.data.append(tmp_list)
        self.loaded = True

    def clean(self):
        self.data = []
        self.tag = None
        self.loaded = False

    def save(self, dal_driver, file=None):
        if file is None:
            file = self.file
        if file is None:
            raise Exception("Need input file name")
        loaded = True
        if not dal_driver.done():
            dal_driver.load()
            loaded = False
        data = dal_driver.get_data()
        if not loaded:
            dal_driver.clean()
        with open(file, "w", newline="\n") as csv_fp:
            for item in data:
                for i in range(len(item)):
                    item[i] = str(item[i])
                csv_fp.write(",".join(item) + "\n")

    def data(self, index):
        if index < 0 or index > len(self.data):
            return None
        return self.data[index]

    def get_data(self):
        return self.data

    def get_tag(self):
        return self.tag

    def done(self):
        return self.loaded