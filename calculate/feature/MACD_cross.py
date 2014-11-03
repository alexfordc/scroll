__author__ = 'cyh'

import calculate.feature.MACD


def compute(data_list, long=26, short=12, m=9):
    rst = []
    macdlist = calculate.feature.MACD.compute(data_list, long, short, m)
    diff = [item[0] for item in macdlist]
    dea = [item[1] for item in macdlist]
    macd = [item[2] for item in macdlist]
    if len(macd) < 2:
        return [0]
    elif len(macd) < 3:
        return [0, 0]
    else:
        rst.append(0)
        for i in range(1, len(macd) - 1):
            if diff[i - 1] < dea[i - 1] and diff[i + 1] > dea[i + 1]:
                rst.append(1)
            elif diff[i - 1] > dea[i - 1] and diff[i + 1] < dea[i + 1]:
                rst.append(-1)
            else:
                rst.append(0)
        rst.append(0)
    return rst