__author__ = 'ict'


def compute(data_a, data_b):
    return sum([abs(data_a[i] - data_b[i]) for i in range(len(data_a))])