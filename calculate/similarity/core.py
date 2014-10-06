__author__ = 'ict'

from calculate.similarity import cos

callback_index = 0
option_indx = 1

method_set = {
    "cos": (cos, False),
}


def method(mtd, data_a, data_b, option=None):
    if mtd not in method_set:
        raise Exception("No such similarity mothod")
    if len(data_a) != len(data_b):
        raise Exception("Two vecter must have same dimension")
    if method_set[mtd][option_indx]:
        return method_set[mtd][callback_index].compute(data_a, data_b, option)
    else:
        return method_set[mtd][callback_index].compute(data_a, data_b)


def names():
    return list(method_set)