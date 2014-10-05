__author__ = 'ict'

import math


def compute(data_a, data_b):
    if len(data_a) != len(data_b):
        raise Exception("Two vecter must have same dimension")
    return math.sqrt(sum([(data_a[i] - data_b[i]) ** 2 for i in range(len(data_a))]))