__author__ = 'ict'

from calculate.classify.KNN import KNN

# 创建k近邻学习器，使用欧几里得距离。
knn = KNN("euclid")

# 数据组
sample = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2]]
# 标签组
label = [0, 0, 0, 1, 1, 1]
# k值
k = 3

# 训练分类器
knn.train(sample, label, k)

#测试分类器对新样本的分类
print(knn.classify([3, 3]))
print(knn.classify([0, 0]))
print(knn.classify([[1, 3], [0, 3]]))