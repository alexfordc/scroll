__author__ = 'ict'

from calculate.classify.SVM import SVM
from service.client import Client

# 数据组
sample = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2]]
# 标签组
label = [0, 0, 0, 1, 1, 1]

# 创建SVM学习器，使用默认参数。
svm = SVM()

# 训练分类器
svm.train(sample, label)

#测试分类器对新样本的分类
print(svm.classify([3, 3]))
print(svm.classify([0, 0]))
print(svm.classify([[1, 3], [0, 3], [0, 2], [0, 1]]))

# 创建服务器连接
c = Client("219.223.243.8", 8088)

# 保存分类器到服务器
c.save(svm, "test")

# 载入之前保存在服务器上的分类器
new_svm = c.load("test")

# 测试新分类器是否和之前的结果一样
print(new_svm.classify([3, 3]))
print(new_svm.classify([0, 0]))
print(new_svm.classify([[1, 3], [0, 3], [0, 2], [0, 1]]))