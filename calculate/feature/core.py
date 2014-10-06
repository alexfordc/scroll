from calculate.helper import MAC

__author__ = 'ict'

from calculate.feature import price_return
from calculate.feature import ratio

callback_index = 0
option_indx = 1

method_set = {
    "price return": (price_return, False),
    "ratio": (ratio, False),
}


def method(mtd, data_list, option=None):
    if mtd not in method_set:
        raise Exception("No such feature mothod")
    if method_set[mtd][option_indx]:
        return method_set[mtd][callback_index].compute(data_list, option)
    else:
        return method_set[mtd][callback_index].compute(data_list)


def names():
    return list(method_set)