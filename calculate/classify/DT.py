__author__ = 'ict'

import copy
import math

from calculate.helper.statistics import entropy


class DT:
    def __init__(self, level=5):
        self.level = level

    def train(self, data, label):
        real_data = copy.deepcopy(data)
        v_set = []
        for i in range(len(real_data[0])):
            i_set = set()
            for d in real_data:
                i_set.add(d[i])
            v_set.append(i_set)
        label_set = set()
        for l in label:
            label_set.add(l)
        l = len(real_data[0])
        label_info = entropy(label)
        for _ in range(l):
            gain = []
            count = {}
            for i in range(len(real_data[0])):
                for j in range(len(real_data)):
                    if (i, real_data[j][i], label[j]) not in count:
                        count[(i, real_data[j][i], label[j])] = 0
                    count[(i, real_data[j][i], label[j])] += 1
            for i in range(len(real_data[0])):
                total_sum_count = 0
                sub_info = 0
                sub_info_list = []
                for v in v_set[i]:
                    count_class = {}
                    v_sub_info = 0
                    for c in label_set:
                        if (i, v, c) in count:
                            count_class[c] = count[(i, v, c)]
                        else:
                            count_class[c] = 0
                    sum_count = sum([v for _, v in count_class.items()])
                    total_sum_count += sum_count
                    for key, _v in count_class.items():
                        if _v != 0:
                            v_sub_info -= (_v / sum_count) * math.log(_v / sum_count)
                    v_sub_info *= sum_count
                    sub_info_list.append(v_sub_info)
                sub_info = sum([info / total_sum_count for info in sub_info_list])



    def classify(self, data):