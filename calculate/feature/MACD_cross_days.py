__author__ = 'cyh'

import calculate.feature.MACD_cross


def compute(data_list, long=26, short=12, m=9):
    rst = []
    mc = calculate.feature.MACD_cross.compute(data_list, long, short, m)
    cross_tag = 0
    for i in range(len(mc)):
        if cross_tag == 0:
            if mc[i] == 0:
                rst.append(0)
            elif mc[i] == 1:
                rst.append(1)
                cross_tag = 1
            elif mc[i] == -1:
                rst.append(-1)
                cross_tag = -1
        elif cross_tag == 1:
            if mc[i] == 0:
                rst.append(rst[i - 1] + 1)
            elif mc[i] == 1:
                rst.append(1)
            elif mc[i] == -1:
                rst.append(-1)
                cross_tag = -1
        elif cross_tag == -1:
            if mc[i] == 0:
                rst.append(rst[i - 1] - 1)
            elif mc[i] == -1:
                rst.append(-1)
            elif mc[i] == 1:
                rst.append(1)
                cross_tag = 1
    return rst