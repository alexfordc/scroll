__author__ = 'ict'

from calculate.helper.SVD import *
import DAL.yahoo

# 读取yahoo股票数据
data = DAL.yahoo.mysqldb("219.223.251.24", "root", None, "stock", "adjclose")

# 构建测试dict
test_dict = {
    1: [1, 2, 3, 4, 5, 6, 7, 8],
    2: [2, 3, 4, 5, 6, 7, 8, 1],
    3: [3, 4, 5, 6, 7, 8, 1, 2],
    4: [4, 5, 6, 7, 8, 1, 2, 3],
}

# SVD降到90%的结果
print(svd(test_dict))
print(svd(data))