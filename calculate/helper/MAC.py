__author__ = 'ict'

# MA crossover


def mac(data_list, x, y, offset=0):
    max_v = max(x, y)
    ma_x = [0] * (max_v - offset + 1)
    ma_y = [0] * (max_v - offset + 1)
    for i in range(max_v - offset, len(data_list) - offset):
        ma_x.append(sum(data_list[i - x + 1 + offset: i + 1 + offset]) / x)
        ma_y.append(sum(data_list[i - y + 1 + offset: i + 1 + offset]) / y)
    rst = [0] * len(data_list)
    for i in range(max_v - offset + 1, len(data_list) - offset):
        if ma_x[i - 1] < ma_y[i - 1] and ma_x[i] > ma_y[i]:
            rst[i] = 1
        if ma_x[i - 1] > ma_y[i - 1] and ma_x[i] < ma_y[i]:
            rst[i] = -1
    return rst