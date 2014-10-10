__author__ = 'ict'

open_offset = 0
high_offset = 1
low_offset = 2
close_offset = 3


def compute(multidata_list, n, ohlc=(0, 1, 2, 3)):
    close_list = [data[ohlc[close_offset]] for data in multidata_list]
    high_list = [data[ohlc[high_offset]] for data in multidata_list]
    low_list = [data[ohlc[low_offset]] for data in multidata_list]
    rsv_list = [50] * (n - 1)
    for i in range(n - 1, len(multidata_list)):
        n_low = min(low_list[i + 1 - n: i + 1])
        rsv_list.append(close_list[i] - n_low)
        sub = max(high_list[i + 1 - n: i + 1]) - n_low
        if sub == 0:
            rsv_list[i] = 0.5
        else:
            rsv_list[i] /= sub
        rsv_list[i] *= 100
    return rsv_list