__author__ = 'ict'

from calculate.helper.PCA import *
import DAL.yahoo

# 读取yahoo股票数据
data = DAL.yahoo.mysqldb("219.223.251.24", "root", None, "stock", "adjclose")

# 构建测试dict
test_dict = {
    1: [1, 2, 3, 4],
    2: [2, 3, 4, 1],
    3: [3, 4, 1, 2],
    4: [4, 1, 2, 3],
}

# PCA降为一维之后的结果
print(pca(test_dict, 1))
print(pca(data, 1))