__author__ = 'cyh'


def compute(data_list, n=3):
    ema_list = [data_list[0]]
    p1 = 2 / (n + 1)
    p2 = 1 - p1
    for i in range(1, len(data_list)):
        ema_value = p1 * data_list[i] + p2 * ema_list[-1]
        ema_list.append(ema_value)
    return ema_list