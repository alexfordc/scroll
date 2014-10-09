__author__ = 'ict'

from calculate.feature import price_return
from calculate.feature import ratio
from calculate.feature import MA_cross

callback_index = 0
option_indx = 1

method_set = {
    "price return": (price_return, False),
    "ratio": (ratio, False),
    "MA cross": (MA_cross, True),
}


def method(mtd, data_list, option=None):
    mtd_list = mtd.split(",")
    for i in range(len(mtd_list)):
        while True:
            if len(mtd_list[i]) == 0:
                raise Exception("Miss method")
            if mtd_list[i][0] == " ":
                mtd_list[i] = mtd_list[i][1:]
            if mtd_list[i][-1] == " ":
                mtd_list[i] = mtd_list[i][:-1]
            if mtd_list[i][0] != " " and mtd_list[i][-1] != " ":
                break
    if len(mtd_list) == 1:
        option = [option]
    if option is None:
        option = [None] * len(mtd_list)
    rst = []
    for i in range(len(mtd_list)):
        if mtd_list[i] not in method_set:
            raise Exception("No such feature mothod: " + mtd)
        if method_set[mtd_list[i]][option_indx] and option[i] is not None:
            rst.append(method_set[mtd_list[i]][callback_index].compute(data_list, option[i]))
        else:
            rst.append(method_set[mtd_list[i]][callback_index].compute(data_list))
    if len(rst) == 1:
        return rst[0]
    else:
        return rst


def names():
    return list(method_set)