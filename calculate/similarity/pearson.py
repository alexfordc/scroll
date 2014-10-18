__author__ = 'ict'

import numpy


def compute(data_a, data_b):
    return numpy.corrcoef(data_a, data_b)