__author__ = 'ict'

from calculate.feature import price_return
from calculate.feature import ratio

method_set = {
    "price return": price_return,
    "ratio": ratio,
}


def method(mtd, data_list):
    if mtd not in method_set:
        raise Exception("No such feature mothod")
    return method_set[mtd].compute(data_list)


def names():
    return list(method_set)