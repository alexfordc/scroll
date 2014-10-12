__author__ = 'cyh'


def compute(data_list, n=3, m=1):
    sma_list = [data_list[0]]
    p1 = m / n
    p2 = 1 - p1
    for i in range(1, len(data_list)):
        sma_value = p1 * data_list[i] + p2 * sma_list[-1]
        sma_list.append(sma_value)
    return sma_list