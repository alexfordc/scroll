__author__ = 'ict'


def compute(data_list):
    rst = []
    if len(data_list) < 2:
        return data_list
    for i in range(len(data_list) - 1):
        rst.append(data_list[i + 1] / data_list[i] - 1)
    return rst