__author__ = 'ict'

import math


def compute(data_a, data_b):
    return math.sqrt(sum([(data_a[i] - data_b[i]) ** 2 for i in range(len(data_a))]))