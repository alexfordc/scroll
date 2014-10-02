__author__ = 'ict'

import math


def mean(data_list):
    if len(data_list) == 0:
        return 0
    return sum(data_list) / len(data_list)


def variance(data_list, option="normal"):
    if len(data_list) == 0:
        return 0
    if len(data_list) == 1:
        return 0
    m = mean(data_list)
    v = 0
    for x in data_list:
        v += (x - m) * (x - m)
    if option == "normal":
        return v / (len(data_list) - 1)
    if option == "standard":
        return math.sqrt(v / (len(data_list) - 1))