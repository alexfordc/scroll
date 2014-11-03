__author__ = 'cyh'

import calculate.feature.KDJ_cross


def compute(multidata_list, n=9, m1=3, m2=3, ohlc=(0, 1, 2, 3)):
    rst = []
    kc = calculate.feature.KDJ_cross.compute(multidata_list, n, m1, m2, ohlc)
    cross_tag = 0
    for i in range(len(kc)):
        if cross_tag == 0:
            if kc[i] == 0:
                rst.append(0)
            elif kc[i] == 1:
                rst.append(1)
                cross_tag = 1
            elif kc[i] == -1:
                rst.append(-1)
                cross_tag = -1
        elif cross_tag == 1:
            if kc[i] == 0:
                rst.append(rst[i - 1] + 1)
            elif kc[i] == 1:
                rst.append(1)
            elif kc[i] == -1:
                rst.append(-1)
                cross_tag = -1
        elif cross_tag == -1:
            if kc[i] == 0:
                rst.append(rst[i - 1] - 1)
            elif kc[i] == -1:
                rst.append(-1)
            elif kc[i] == 1:
                rst.append(1)
                cross_tag = 1
    return rst