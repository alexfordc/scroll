__author__ = 'ict'

# MA crossover


def mac(data_list, x, y, offset=0):
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


def ma(data_list, w, offset=0, start=-1):
    if start == -1:
        start = w
    ma_list = []
    for i in range(start - offset, len(data_list) - offset):
        ma_list.append(sum(data_list[i - w + 1 + offset: i + 1 + offset]) / w)
    return ma_list