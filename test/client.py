__author__ = 'ict'

from service.client import Client

# 测试用的变量
test = {
    1: [1, 2, 3],
    2: [1, 2, 3],
    3: [1, 2, 3],
}

# 创建一个到服务器的连接
c = Client("219.223.243.8", 8088)

# 测试对变量的各种存取操作
print(c.save(test, "test"))

print(c.load("test"))

print(c.list())

print(c.remove("test"))

print(c.load("test"))

print(c.list())

# 关闭连接
c.close()