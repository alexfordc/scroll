__author__ = 'ict'

from calculate.helper.stock import ma


def compute(data_list, option):
    x = option[0]
    y = option[1]
    offset = 0
    if len(option) > 2:
        offset = option[2]
    if x >= y:
        raise Exception("x must less than y")
    ma_x = [0] * (y - offset + 1) + ma(data_list, x, offset, start=y)
    ma_y = [0] * (y - offset + 1) + ma(data_list, y, offset, start=y)
    rst = [0] * len(data_list)
    for i in range(y - offset + 1, len(data_list) - offset):
        if ma_x[i - 1] < ma_y[i - 1] and ma_x[i] > ma_y[i]:
            rst[i] = 1
        if ma_x[i - 1] > ma_y[i - 1] and ma_x[i] < ma_y[i]:
            rst[i] = -1
    return rst