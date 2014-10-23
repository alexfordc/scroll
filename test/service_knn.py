__author__ = 'ict'

from calculate.classify.KNN import KNN
from service.client import Client

# 数据组
sample = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2]]
# 标签组
label = [0, 0, 0, 1, 1, 1]
# k值
k = 3

# 创建k近邻学习器，使用欧几里得距离。
knn = KNN(k)

# 训练分类器
knn.train(sample, label)

# 测试分类器对新样本的分类
print(knn.classify([3, 3]))
print(knn.classify([0, 0]))
print(knn.classify([[1, 3], [0, 3]]))

# 创建服务器连接
c = Client("219.223.243.8", 8088)

# 保存分类器到服务器
c.save(knn, "test-knn")

# 载入之前保存在服务器上的分类器
new_knn = c.load("test-knn")

# 测试新分类器是否和之前的结果一样
print(new_knn.classify([3, 3]))
print(new_knn.classify([0, 0]))
print(new_knn.classify([[1, 3], [0, 3]]))