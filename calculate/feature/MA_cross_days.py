__author__ = 'cyh'

import calculate.feature.MA_cross


def compute(data_list, x=9, y=3, offset=0):
    rst = []
    ma = calculate.feature.MA_cross.compute(data_list, x, y, offset)
    cross_tag = 0
    for i in range(len(ma)):
        if cross_tag == 0:
            if ma[i] == 0:
                rst.append(0)
            elif ma[i] == 1:
                rst.append(1)
                cross_tag = 1
            elif ma[i] == -1:
                rst.append(-1)
                cross_tag = -1
        elif cross_tag == 1:
            if ma[i] == 0:
                rst.append(rst[i - 1] + 1)
            elif ma[i] == 1:
                rst.append(1)
            elif ma[i] == -1:
                rst.append(-1)
                cross_tag = -1
        elif cross_tag == -1:
            if ma[i] == 0:
                rst.append(rst[i - 1] - 1)
            elif ma[i] == -1:
                rst.append(-1)
            elif ma[i] == 1:
                rst.append(1)
                cross_tag = 1
    return rst