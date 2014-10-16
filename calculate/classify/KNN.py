__author__ = 'ict'

import DAL.file
import calculate.distance.core


class KNN:
    def __init__(self, k=1, distance="euclid", option=None):
        self.sample = []
        self.distance = calculate.distance.core.get_function(distance)
        self.option = option
        self.k = k

    def train(self, data, label):
        if len(data) != len(label):
            raise Exception("data and label must have same dimension")
        self.sample = [(data[i], label[i]) for i in range(len(data))]

    def classify(self, data):
        if len(data) == 0:
            raise Exception("Null data list")
        user_no_list = False
        if not isinstance(data[0], list):
            data = [data]
            user_no_list = True
        rst = []
        for one_data in data:
            d = []
            for samp in self.sample:
                if self.option is not None:
                    d.append((self.distance(one_data, samp[0], self.option), samp[1]))
                else:
                    d.append((self.distance(one_data, samp[0]), samp[1]))
            d.sort()
            if self.k < len(d):
                dknn = d[:self.k]
            else:
                dknn = d
            label_sum = {}
            for candi in dknn:
                if candi[1] not in label_sum:
                    label_sum[candi[1]] = 0
                label_sum[candi[1]] += 1
            rst.append(max([(count, label) for label, count in label_sum.items()])[1])
        if user_no_list:
            return rst[0]
        return rst

    def save(self, file):
        DAL.file.save((self.sample, self.k), file)

    def load(self, file):
        (self.sample, self.k) = DAL.file.load(file)