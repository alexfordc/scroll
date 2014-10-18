__author__ = 'ict'

import calculate.distance.euclid


def compute(data_a, data_b):
    return 1 / (1 + calculate.distance.euclid.compute(data_a, data_b))