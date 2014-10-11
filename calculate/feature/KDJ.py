__author__ = 'ict'

import calculate.feature.RSV
import calculate.feature.MA


def compute(data_list, n, m1, m2, ohlc=(0, 1, 2, 3)):
    rsv_list = calculate.feature.RSV.compute(data_list, n, ohlc)
    k_p1 = (m1 - 1) / m1
    k_p2 = 1 / m1
    d_p1 = (m2 - 1) / m2
    d_p2 = 1 / m2
    k = [50]
    d = [50, 50]
    for i in range(1, len(rsv_list)):
        k.append(k_p1 * k[i - 1] + k_p2 * rsv_list[i])
    for i in range(2, len(k)):
        d.append(d_p1 * d[i - 1] + d_p2 * k[i])
    return [[k[i], d[i], 3 * k[i] - 2 * d[i]] for i in range(len(data_list))]