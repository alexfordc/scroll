__author__ = 'ict'

from calculate.similarity import cos

method_set = {
    "cos": cos,
}


def method(mtd, data_a, data_b):
    if mtd not in method_set:
        raise Exception("No such similarity mothod")
    return method_set[mtd].compute(data_a, data_b)


def names():
    return list(method_set)