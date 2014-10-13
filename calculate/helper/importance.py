__author__ = 'ict'

from calculate.helper.statistics import variance


def importance(data_dict):
    weight_list = []
    tmp = data_dict.popitem()
    data_dict[tmp[0]] = tmp[1]
    for i in range(len(tmp[1])):
        weight_list.append(variance([value[i] for _, value in data_dict.items()]))
    for key, value in data_dict.items():
        data_dict[key] = [weight_list[i] * value[i] for i in range(len(tmp[1]))]