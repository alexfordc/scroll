__author__ = 'ict'

import calculate.similarity.pearson


def compute(data_a, data_b):
    return 1 / calculate.similarity.pearson.compute(data_a, data_b) - 1