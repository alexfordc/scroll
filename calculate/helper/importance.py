__author__ = 'ict'

from calculate.helper.statistics import variance
from calculate.helper.statistics import entropy
from calculate.helper.statistics import gini
import math


def importance(data_dict, method="standard variance"):
    weight_list = []
    tmp = data_dict.popitem()
    data_dict[tmp[0]] = tmp[1]
    for i in range(len(tmp[1])):
        if method == "standard variance":
            weight_list.append(math.sqrt(variance([value[i] for _, value in data_dict.items()])))
        elif method == "variance":
            weight_list.append(variance([value[i] for _, value in data_dict.items()]))
        elif method == "entropy":
            weight_list.append(entropy([value[i] for _, value in data_dict.items()]))
        elif method == "gini":
            weight_list.append(gini([value[i] for _, value in data_dict.items()]))
        else:
            raise Exception("Invalid method: " + str(method))
    for key, value in data_dict.items():
        data_dict[key] = [weight_list[i] * value[i] for i in range(len(tmp[1]))]