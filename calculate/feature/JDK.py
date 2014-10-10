__author__ = 'ict'

import calculate.feature.RSV
import calculate.feature.MA


def compute(data_list, n, m, m1, ohlc=(0, 1, 2, 3)):
    rsv_list = calculate.feature.RSV.compute(data_list, n, ohlc)
    k = calculate.feature.MA.compute(rsv_list, m)
    d = calculate.feature.MA.compute(k, m1)
    k = [50] * (m - 1) + k
    d = [50] * (m - 1 + m1 - 1) + d
    return [[k[i], d[i], 3 * k[i] - 2 * d[i]] for i in range(len(data_list))]