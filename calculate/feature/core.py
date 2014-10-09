__author__ = 'ict'

from calculate.feature import price_return
from calculate.feature import ratio
from calculate.feature import MA_cross

callback_index = 0
option_indx = 1
multidata_index = 2

# (callback, have index, multidata)
method_set = {
    "price return": (price_return, False, False),
    "ratio": (ratio, False, False),
    "MA cross": (MA_cross, True, False),
}


def method(mtd, data_list, option=None):
    single_data_list = None
    if isinstance(data_list[0], list):
        multidata = True
        single_data_list = [data[0] for data in data_list]
    else:
        multidata = False
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
            raise Exception("No such feature method: " + str(mtd_list[i]))
        if not multidata and method_set[mtd_list[i]][multidata_index]:
            raise Exception("This method need multidata: " + str(mtd_list[i]))
        if multidata and not method_set[mtd_list[i]][multidata_index]:
            _data_list = single_data_list
        else:
            _data_list = data_list
        if method_set[mtd_list[i]][option_indx] and option[i] is not None:
            rst.append(method_set[mtd_list[i]][callback_index].compute(_data_list, option[i]))
        else:
            rst.append(method_set[mtd_list[i]][callback_index].compute(_data_list))
    if len(rst) == 1:
        return rst[0]
    else:
        return rst


def get_function(mtd):
    if mtd not in method_set:
        raise Exception("No such cluster method: " + str(mtd))
    return method_set[mtd][callback_index].compute


def names():
    return list(method_set)