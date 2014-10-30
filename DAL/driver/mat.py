__author__ = 'ict'

import os

import scipy.io
from DAL.driver.base import Base


class Mat(Base):
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
        self.tag = scipy.io.whosmat(file)[0][0]
        self.data = scipy.io.loadmat(file)[self.tag].tolist()
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
        tag = dal_driver.get_tag()
        if not loaded:
            dal_driver.clean()
        scipy.io.savemat(file, {tag: data})