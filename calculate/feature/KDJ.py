__author__ = 'ict'

import calculate.feature.RSV
import calculate.feature.SMA


def compute(data_list, n, m1, m2, ohlc=(0, 1, 2, 3)):
    rsv_list = calculate.feature.RSV.compute(data_list, n, ohlc)
    k = calculate.feature.SMA.compute(rsv_list, m1, 1)
    d = [50] + calculate.feature.SMA.compute(k, m2, 1)
    return [[k[i], d[i], 3 * k[i] - 2 * d[i]] for i in range(len(data_list))]