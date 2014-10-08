__author__ = 'ict'


def ma(data_list, w, offset=0, start=-1):
    if start == -1:
        start = w
    ma_list = []
    for i in range(start - offset, len(data_list) - offset):
        ma_list.append(sum(data_list[i - w + 1 + offset: i + 1 + offset]) / w)
    return ma_list