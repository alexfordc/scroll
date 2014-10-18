__author__ = 'ict'

import numpy


def pca(data_dict, n=0):
    data = []
    keys = []
    for key, value in data_dict.items():
        data.append(value)
        keys.append(key)
    data_mat = numpy.mat(data)
    if n == 0:
        n = numpy.shape(data_mat)[0]
    mean_mat = numpy.mean(data_mat, axis=0)
    normal_mat = data_mat - mean_mat
    cov_mat = numpy.cov(normal_mat, rowvar=0)
    eigen_value, eigen_vector = numpy.linalg.eig(numpy.mat(cov_mat))
    eigen_value_index = numpy.argsort(eigen_value)[: -(n + 1): -1]
    reduce_eigen_vector = eigen_vector[:, eigen_value_index]
    pca_rst = normal_mat * reduce_eigen_vector
    n = numpy.shape(pca_rst)[-1]
    rst_dict = {}
    for i in range(len(keys)):
        rst_dict[keys[i]] = [pca_rst[i, j].real for j in range(n)]
    return rst_dict