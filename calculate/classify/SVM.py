__author__ = 'ict'

from extern.libsvm.svmutil import *

svm_type = {
    "C-SVC": 0,
    "nu-SVC": 1,
    "one-class SVM": 2,
    "epsilon-SVR": 3,
    "nu-SVR": 4
}

kernel_type = {
    "linear": 0,
    "polynomial": 1,
    "radial basis function": 2,
    "sigmoid": 3,
    "precomputed kernel": 4
}


class SVM:
    def __init__(self, svm=0, kernel=2, degree=3, gamma=1, coef0=0, cost=1, nu=0.5):
        if isinstance(svm, str):
            if svm not in svm_type:
                raise Exception("Invalid svm type: " + svm)
            else:
                self.svm_n = svm_type[svm]
        elif isinstance(svm, int):
            self.svm_n = svm
        else:
            raise Exception("Invalid type of svm type: " + str(type(svm)))
        if isinstance(kernel, str):
            if kernel not in kernel_type:
                raise Exception("Invalid svm type: " + kernel)
            else:
                self.kernel_n = kernel_type[kernel]
        elif isinstance(kernel, int):
            self.kernel_n = kernel
        else:
            raise Exception("Invalid type of svm type: " + str(type(kernel)))
        self.degree = degree
        self.gamma = gamma
        self.coef0 = coef0
        self.cost = cost
        self.nu = nu
        self.svm = None

    def train(self, data, label):
        if len(data) != len(label):
            raise Exception("data and label must have same dimension")
        data_dict = []
        if isinstance(data[0], list):
            for d in data:
                d_dict = {}
                for _i in range(len(d)):
                    d_dict[_i + 1] = d[_i]
                data_dict.append(d_dict)
        elif isinstance(data[0], dict):
            data_dict = data
        else:
            raise Exception("Invalid train data type: " + str(type(data[0])))
        param = "-q -s %d -t %d -d %d -g %d -r %d" % (self.svm_n, self.kernel_n, self.degree, self.gamma, self.coef0)
        if self.svm_n in [svm_type["C-SVC"], svm_type["epsilon-SVR"], svm_type["nu-SVR"]]:
            param += " -c %d" % self.cost
        if self.svm_n in [svm_type["nu-SVC"], svm_type["one-class SVM"], svm_type["nu-SVR"]]:
            param += " -n %d" % self.nu
        self.svm = svm_train(label, data_dict, param)

    def classify(self, data):
        if self.svm is None:
            raise Exception("Need train first")
        if len(data) == 0:
            raise Exception("Null data list")
        user_no_list = False
        if not isinstance(data[0], list):
            data = [data]
            user_no_list = True
        data_dict = []
        if isinstance(data[0], list):
            for d in data:
                d_dict = {}
                for _i in range(len(d)):
                    d_dict[_i + 1] = d[_i]
                data_dict.append(d_dict)
        elif isinstance(data[0], dict):
            data_dict = data
        else:
            raise Exception("Invalid train data type: " + str(type(data[0])))
        rst, _, _ = svm_predict([1] * len(data_dict), data_dict, self.svm, "-q")
        if user_no_list:
            return rst[0]
        return rst

    def save(self, file):
        svm_save_model(file, self.svm)

    def load(self, file):
        self.svm = svm_load_model(file)