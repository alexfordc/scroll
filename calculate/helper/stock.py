__author__ = 'ict'


def ma(data_list, w, offset=0, start=-1):
    if start == -1:
        start = w
    ma_list = []
    for i in range(start - offset, len(data_list) - offset):
        ma_list.append(sum(data_list[i - w + 1 + offset: i + 1 + offset]) / w)
    return ma_list


open_offset = 0
high_offset = 1
low_offset = 2
close_offset = 3


def rsv(multidata_list, n, ohlc=(0, 1, 2, 3)):
    close_list = [data[ohlc[close_offset]] for data in multidata_list]
    high_list = [data[ohlc[high_offset]] for data in multidata_list]
    low_list = [data[ohlc[low_offset]] for data in multidata_list]
    rsv_list = [50] * (n - 1)
    for i in range(n - 1, len(multidata_list)):
        n_low = min(low_list[i + 1 - n: i + 1])
        rsv_list[i] = (close_list[i] - n_low)
        rsv_list[i] /= (max(high_list[i + 1 - n: i + 1]) - n_low)
        rsv_list[i] *= 100