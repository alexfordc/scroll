__author__ = 'ict'

import math


def compute(data_list):
    rst = []
    if len(data_list) < 2:
        return data_list
    for i in range(len(data_list) - 1):
        rst.append(math.log(data_list[i + 1] / data_list[i]))
    return rst