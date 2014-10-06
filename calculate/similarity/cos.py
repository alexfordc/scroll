__author__ = 'ict'

import math


def compute(data_a, data_b):
    norm_ab = 0
    norm_a = 0
    norm_b = 0
    for i in range(len(data_a)):
        norm_ab += data_a[i] * data_b[i]
        norm_a += data_a[i] * data_a[i]
        norm_b += data_b[i] * data_b[i]
    if norm_a == 0 or norm_b == 0:
        return 0
    return abs(norm_ab) / math.sqrt(norm_a * norm_b)