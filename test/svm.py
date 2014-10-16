__author__ = 'ict'

from calculate.classify.SVM import SVM

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

# 保存分类器
svm.save(r"e:\svm.ict")

# 创建一个新的svm分类器
new_svm = SVM()

# 载入之前保存的分类器
new_svm.load(r"e:\svm.ict")

# 测试新分类器是否和之前的结果一样
print(new_svm.classify([3, 3]))
print(new_svm.classify([0, 0]))
print(new_svm.classify([[1, 3], [0, 3], [0, 2], [0, 1]]))