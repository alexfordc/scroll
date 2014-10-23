__author__ = 'ict'

from calculate.feature import price_return
from calculate.feature import change_rate
from calculate.feature import MA_cross
from calculate.feature import MA
from calculate.feature import RSV
from calculate.feature import KDJ
from calculate.feature import EMA
from calculate.feature import MACD
from calculate.feature import SMA
from calculate.feature import FFT

callback_index = 0
option_indx = 1
multidata_index = 2

# (callback, have option, multidata)
method_set = {
    "price return": (price_return, False, False),
    "change rate": (change_rate, False, False),
    "MA cross": (MA_cross, True, False),
    "MA": (MA, True, False),
    "RSV": (RSV, True, True),
    "KDJ": (KDJ, True, True),
    "EMA": (EMA, True, False),
    "MACD": (MACD, True, False),
    "SMA": (SMA, True, False),
    "FFT": (FFT, True, False),
}


def method(mtd, data_list, option=None, main=None, unpack=False):
    single_data_list = []
    if isinstance(data_list[0], list):
        multidata = True
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
    for i in range(len(mtd_list)):
        if mtd_list[i] not in method_set:
            raise Exception("No such feature method: " + str(mtd_list[i]))
        if main is None:
            if multidata and not method_set[mtd_list[i]][multidata_index]:
                raise Exception("Need give main data index when input multidata")
            single_data_list.append(None)
        else:
            if multidata:
                if main[i] is None:
                    if not method_set[mtd_list[i]][multidata_index]:
                        raise Exception("Need give main data index for a non-mulidata method: " + str(mtd_list[i]))
                    single_data_list.append(None)
                else:
                    single_data_list.append([data[main[i]] for data in data_list])
    rst = []
    for i in range(len(mtd_list)):
        if not multidata and method_set[mtd_list[i]][multidata_index]:
            raise Exception("This method need multidata: " + str(mtd_list[i]))
        if multidata and not method_set[mtd_list[i]][multidata_index]:
            _data_list = single_data_list[i]
        else:
            _data_list = data_list
        if method_set[mtd_list[i]][option_indx] and option[i] is not None:
            if isinstance(option[i], dict):
                rst.append(method_set[mtd_list[i]][callback_index].compute(_data_list, **option[i]))
            else:
                rst.append(method_set[mtd_list[i]][callback_index].compute(_data_list, option[i]))
        else:
            rst.append(method_set[mtd_list[i]][callback_index].compute(_data_list))
    if unpack:
        new_rst = []
        for ft in rst:
            if isinstance(ft, list):
                new_rst.extend(ft)
            else:
                new_rst.append(ft)
    else:
        new_rst = rst
    if len(new_rst) == 1:
        return new_rst[0]
    else:
        return new_rst


def get_function(mtd):
    if mtd not in method_set:
        raise Exception("No such cluster method: " + str(mtd))
    return method_set[mtd][callback_index].compute


def names():
    return list(method_set)