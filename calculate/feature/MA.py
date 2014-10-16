__author__ = 'ict'


def compute(data_list, w, offset=0):
    ma_list = []
    for i in range(-offset, len(data_list) - offset):
        if i < w - offset - 1:
            ma_list.append(sum(data_list[: i + 1 + offset]) / (i + 1 + offset))
        else:
            ma_list.append(sum(data_list[i - w + 1 + offset: i + 1 + offset]) / w)
    return ma_list