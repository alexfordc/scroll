__author__ = 'cyh'

import calculate.feature.KDJ


def compute(multidata_list, n=9, m1=3, m2=3, ohlc=(0, 1, 2, 3)):
    rst = []
    kdj = calculate.feature.KDJ.compute(multidata_list, n, m1, m2, ohlc)
    k = [item[0] for item in kdj]
    d = [item[1] for item in kdj]
    if len(k) < 2:
        return [0]
    elif len(k) < 3:
        return [0, 0]
    else:
        rst.append(0)
        for i in range(1, len(k) - 1):
            if k[i - 1] < d[i - 1] and k[i + 1] > d[i + 1]:
                rst.append(1)
            elif k[i - 1] > d[i - 1] and k[i + 1] < d[i + 1]:
                rst.append(-1)
            else:
                rst.append(0)
        rst.append(0)
    return rst