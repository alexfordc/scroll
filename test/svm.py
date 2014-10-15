__author__ = 'ict'

from calculate.classify.SVM import SVM

# 数据组
sample = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2]]
# 标签组
label = [0, 0, 0, 1, 1, 1]

# 创建k近邻学习器，使用欧几里得距离。
svm = SVM()

# 训练分类器
svm.train(sample, label)

#测试分类器对新样本的分类
print(svm.classify([3, 3]))
print(svm.classify([0, 0]))
print(svm.classify([[1, 3], [0, 3], [0, 2], [0, 1]]))