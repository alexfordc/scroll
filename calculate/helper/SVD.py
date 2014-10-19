__author__ = 'ict'

import numpy


def svd(data_dict, r=0.9):
    if r < 0 or r > 1:
        raise Exception("r must in [0, 1]")
    data = []
    keys = []
    for key, value in data_dict.items():
        data.append(value)
        keys.append(key)
    data_mat = numpy.mat(data)
    u, sigma, vt = numpy.linalg.svd(data_mat.T)
    n = 0
    max_power = sum(sigma)
    for i in range(1, len(sigma) + 1):
        if sum(sigma[:i]) >= r * max_power:
            n = i
            break
    reduce_mat = data_mat * u[:, : n] * numpy.mat(numpy.eye(n) * sigma[:n])
    rst_dict = {}
    for i in range(len(keys)):
        rst_dict[keys[i]] = [reduce_mat[i, j].real for j in range(n)]
    return rst_dict