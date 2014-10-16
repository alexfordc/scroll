__author__ = 'ict'

import DAL.yahoo  # 读取yahoo股票数据
import calculate.feature.core

# 这段代码测试所有特征的计算

# 读取存放在e盘下的yahoo股票数据，使用数据中的所有价格数据。
data = DAL.yahoo.csv(r"e:\stockdata", "open high low close adjclose")

# 选择要计算的所有特征名称
mtd_str = "MA, MA cross, price return, change rate, RSV, KDJ, EMA, MACD, SMA"

# 针对每个特征计算方法的参数
option = [
    {
        "w": 10,
        "offset": 0
    },
    {
        "x": 3,
        "y": 5,
        "offset": 0,
    },
    None,
    None,
    {
        "n": 10,
        "ohlc": (0, 1, 2, 3),
    },
    {
        "n": 10,
        "m1": 3,
        "m2": 3,
    },
    {
        "n": 12
    },
    {
        "long": 26,
        "short": 12,
        "m": 9,
    },
    {
        "n": 4,
        "m": 2,
    }
]

# 所有非multidata的方法的main值
main = [4, 4, 4, 4, None, None, 4, 4, 4]

# 计算每个数据的所有特征并打印
for key, value in data.items():
    print(calculate.feature.core.method(mtd_str, value, option, main))