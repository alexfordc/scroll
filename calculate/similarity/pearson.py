__author__ = 'ict'

import numpy


def compute(data_a, data_b):
    return 0.5 + 0.5 * numpy.corrcoef(data_a, data_b)[0][1]