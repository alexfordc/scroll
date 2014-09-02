__author__ = 'ict'

import math


def compute(data_a, data_b):
    l = min(len(data_a), len(data_b))
    norm_ab = 0
    norm_a = 0
    norm_b = 0
    for i in range(l):
        norm_ab += data_a[i] * data_b[i]
        norm_a += data_a[i] * data_a[i]
        norm_b += data_b[i] * data_b[i]
    return abs(norm_ab) / math.sqrt(norm_a * norm_b)