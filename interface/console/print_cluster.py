__author__ = 'ict'

import re
from interface.helper.stock_info import stock_name


def print_cluster(cluster_set):
    for one_set in cluster_set:
        one_list = list(one_set)
        for i in range(len(one_list)):
            stock_id = re.findall(r"\d{6}", one_list[i])[0]
            print("%s(%s)" % (stock_name(stock_id), stock_id), end="")
            if i != len(one_list) - 1:
                print(", ", end="")
        print("")