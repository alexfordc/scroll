__author__ = 'ict'

from DAL.driver.base import Base


# stock dict
class SD(Base):
    def __init__(self, mapping=None):
        Base.__init__(self)
        self.mapping = mapping
        self.data = []

    def load(self, mapping=None):
        if mapping is None:
            mapping = self.mapping
        if mapping is None:
            raise Exception("Need input a mapping")
        self.data = []
        for key, value in mapping.items():
            self.data.append([key] + value)

    def save(self, dal_driver):
        pass