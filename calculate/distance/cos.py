__author__ = 'ict'

import calculate.similarity.cos


def compute(data_a, data_b):
    return 1 - calculate.similarity.cos.compute(data_a, data_b)