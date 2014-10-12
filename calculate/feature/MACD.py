__author__ = 'cyh'

import calculate.feature.EMA


def compute(data_list, long=26, short=12, m=9):
    diff = []
    macd = []
    if short < 0 or long < 0 or m < 0:
        raise Exception("para.short and para.long and para.m must be positive")
    if short >= long:
        raise Exception("para.short must less than para.long")
    diff_short = calculate.feature.EMA.compute(data_list, short)
    diff_long = calculate.feature.EMA.compute(data_list, long)
    for i in range(len(diff_long)):
        diff.append(diff_short[i] - diff_long[i])
    dea = calculate.feature.EMA.compute(diff, m)
    for i in range(len(diff)):
        macd.append(2 * (diff[i] - dea[i]))
    return [[diff[i], dea[i], macd[i]] for i in range(len(diff))]