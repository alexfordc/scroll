__author__ = 'ict'

import pickle


def save(var, filename):
    try:
        fp = open(filename, "wb")
        pickle.dumps(var, fp)
    except:
        raise Exception("Can not open file: " + filename)


def load(filename):
    try:
        fp = open(filename, "rb")
        return pickle.load(fp)
    except:
        raise Exception("Can not open file: " + filename)