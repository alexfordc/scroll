__author__ = 'ict'

from calculate.helper.FFT import fft


def compute(data_list, start=0, end=0):
    if end == 0:
        return fft(data_list)[start:]
    else:
        return fft(data_list)[start: end]