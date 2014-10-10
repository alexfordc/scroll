__author__ = 'ict'

import calculate.feature.MA

x_index = 0
y_index = 1
offset_index = 2


def compute(data_list, x, y, offset=0):
    if x >= y:
        raise Exception("x must less than y")
    ma_x = [0] * (y - offset + 1) + calculate.feature.MA.compute(data_list, x, offset, start=y)
    ma_y = [0] * (y - offset + 1) + calculate.feature.MA.compute(data_list, y, offset, start=y)
    rst = [0] * len(data_list)
    for i in range(y - offset + 1, len(data_list) - offset):
        if ma_x[i - 1] < ma_y[i - 1] and ma_x[i] > ma_y[i]:
            rst[i] = 1
        if ma_x[i - 1] > ma_y[i - 1] and ma_x[i] < ma_y[i]:
            rst[i] = -1
    return rst