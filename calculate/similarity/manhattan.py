__author__ = 'ict'

import calculate.distance.manhattan


def compute(data_a, data_b):
    return 1 / (1 + calculate.distance.manhattan.compute(data_a, data_b))