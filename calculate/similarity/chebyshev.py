__author__ = 'ict'

import calculate.distance.chebyshev


def compute(data_a, data_b):
    return 1 / (1 + calculate.distance.chebyshev.compute(data_a, data_b))