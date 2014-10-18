__author__ = 'ict'

import numpy


def fft(data_list):
    return list(abs(numpy.fft.fft(data_list)))


def fftd(data_dict):
    data = []
    for _, value in data_dict.items():
        data.append(value)
    data_array = numpy.array(data, numpy.float)
    rst_array = abs(numpy.fft.fft2(data_array))
    return [list(a) for a in rst_array]