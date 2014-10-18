__author__ = 'ict'

import calculate.distance.minkowski


def compute(data_a, data_b, p):
    return 1 / (1 + calculate.distance.minkowski.compute(data_a, data_b, p))