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


def entropy(data_list):
    if len(data_list) == 0:
        return 0
    elem_dict = {}
    for data in data_list:
        if data not in elem_dict:
            elem_dict[data] = 0
        elem_dict[data] += 1
    h = 0
    for _, count in elem_dict.items():
        p = count / len(data_list)
        h -= p * math.log(p)
    return h


def gini(data_list):
    if len(data_list) == 0:
        return 0
    elem_dict = {}
    for data in data_list:
        if data not in elem_dict:
            elem_dict[data] = 0
        elem_dict[data] += 1
    g = 1
    for _, count in elem_dict.items():
        p = count / len(data_list)
        g -= p ** 2
    return g


def normalization(data_list, r_min=0, r_max=1):
    if len(data_list) == 0:
        return data_list
    if r_max <= r_min:
        raise Exception("Mapping Range max <= min")
    sub = max(data_list) - min(data_list)
    r_sub = r_max - r_min
    if sub == 0:
        return [r_max] * len(data_list)
    return [(r_sub / sub) * (x - min(data_list)) for x in data_list]