__author__ = 'ict'

from calculate.helper.FFT import *

# 创建list类型的测试数据
test_list = [1, 2, 3, 4, 5, 6, 7, 8]

# 创建dict类型的测试数据
test_dict = {
    1: [1, 2, 3, 4],
    2: [2, 3, 4, 1],
    3: [3, 4, 1, 2],
    4: [4, 1, 2, 3],
}

# 分别使用单次傅里叶变化和针对字典的二维傅里叶变换
print(fft(test_list))
print(fftd(test_dict))