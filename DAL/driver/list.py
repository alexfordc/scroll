__author__ = 'ict'

import os

from DAL.driver.base import Base


class List(Base):
    def __init__(self, file=None):
        Base.__init__(self)
        self.file = file

    def load(self, file=None):
        if file is None:
            file = self.file
        if file is None:
            raise Exception("Need input file name")
        if not os.path.isfile(file):
            raise FileNotFoundError("No such file: " + file)
        self.tag = file.lower()
        with open(file, "r") as l_fp:
            buff = l_fp.read()
        self.data = []
        if "\r\n" in buff:
            buff_list = buff.split("\r\n")
        else:
            buff_list = buff.split("\n")
        for item in buff_list:
            if len(item) == 0:
                continue
            item_list = item.split("\t")
            tmp_list = []
            for each in item_list:
                if len(each) != 0:
                    tmp_list.append(each)
            self.data.append(tmp_list)
        self.loaded = True

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
        with open(file, "w", newline="\n") as l_fp:
            for item in data:
                for i in range(len(item)):
                    item[i] = str(item[i])
                l_fp.write("\t".join(item) + "\n")