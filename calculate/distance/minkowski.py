__author__ = 'ict'


def compute(data_a, data_b, p):
    if p <= 0:
        raise Exception("p must bigger than 0")
    return (sum([abs(data_a[i] - data_b[i]) ** p for i in range(len(data_a))])) ** (1 / p)