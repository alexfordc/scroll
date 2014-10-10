__author__ = 'ict'


def compute(data_list, w, offset=0, start=None):
    if start is None:
        start = w
    ma_list = []
    for i in range(start - offset - 1, len(data_list) - offset):
        ma_list.append(sum(data_list[i - w + 1 + offset: i + 1 + offset]) / w)
    return ma_list