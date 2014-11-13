__author__ = 'ict'

import copy
import math

import DAL.file
from calculate.helper.statistics import entropy

class_index_offset = 0
class_value_offset = 1
result_offset = 2


class DT:
    def __init__(self):
        self.tree = []

    def generate_tree(self, data, label):
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
        label_info = entropy(label)
        gain = []
        count = {}
        for i in range(len(real_data[0])):
            for j in range(len(real_data)):
                if (i, real_data[j][i], label[j]) not in count:
                    count[(i, real_data[j][i], label[j])] = 0
                count[(i, real_data[j][i], label[j])] += 1
        for i in range(len(real_data[0])):
            total_sum_count = 0
            sub_info_list = []
            iv_list = []
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
                iv_list.append(sum_count)
            sub_info = sum([info / total_sum_count for info in sub_info_list])
            iv = sum([-(iv_elem / total_sum_count) * math.log(iv_elem / total_sum_count) for iv_elem in iv_list])
            if iv == 0:
                gain.append(float("inf"))
            else:
                gain.append((label_info - sub_info) / iv)
        max_i = gain.index(max(gain))
        sep_data_dict = {}
        sep_label_dict = {}
        for i in range(len(real_data)):
            if real_data[i][max_i] not in sep_data_dict:
                sep_data_dict[real_data[i][max_i]] = []
                sep_label_dict[real_data[i][max_i]] = []
            key = real_data[i][max_i]
            del real_data[i][max_i]
            sep_data_dict[key].append(real_data[i])
            sep_label_dict[key].append(label[i])
        rst = []
        for key, value in sep_data_dict.items():
            complete = True
            old_v = sep_label_dict[key][0]
            for v in sep_label_dict[key]:
                if v != old_v:
                    complete = False
                    break
            if complete:
                rst.append([max_i, key, old_v])
            else:
                rst.append([max_i, key, self.generate_tree(value, sep_label_dict[key])])
        return rst

    def train(self, data, label):
        if len(data) != len(label):
            raise Exception("data and label must have same dimension")
        self.tree = self.generate_tree(data, label)

    def classify(self, data):
        if len(self.tree) == 0:
            raise Exception("Need train first")
        if len(data) == 0:
            raise Exception("Null data list")
        rst = []
        for d in data:
            d = d.copy()
            nodes = self.tree
            d_rst = None
            while True:
                for node in nodes:
                    if d[node[class_index_offset]] == node[class_value_offset]:
                        d_rst = node[result_offset]
                        del d[node[class_index_offset]]
                        break
                if isinstance(d_rst, list):
                    nodes = d_rst
                else:
                    break
            rst.append(d_rst)
        return rst

    def save(self, file):
        DAL.file.save(self.tree, file)

    def load(self, file):
        self.tree = DAL.file.load(file)