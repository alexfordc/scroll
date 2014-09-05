__author__ = 'ict'


class Base:
    def __init__(self):
        self.data = []
        self.tag = None
        self.loaded = False

    def clean(self):
        self.data = []
        self.tag = None
        self.loaded = False

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