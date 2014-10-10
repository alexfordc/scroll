__author__ = 'ict'

import DAL.yahoo
from interface.gui.kline import Kline
import calculate.feature.core

# 读取yahoo股票数据到data变量
data = DAL.yahoo.csv(r"e:\stockdata", "open high low close volume")

# 取股票代码为600888的数据到d变量
d = data["ss600888"]

# 取出每天的收盘价到dclose变量
dclose = [p[3] for p in d]

# 创建一个k线图类
k = Kline(1800, 900)

# 创建基本k线图
k.create_basic(d)

# 获得计算MA的函数
ma = calculate.feature.core.get_function("MA")

# 分别计算5、10、30天的MA值
ma5 = ma(dclose, 5)
ma10 = ma(dclose, 10)
ma30 = ma(dclose, 30)

# 将MA值添加到k线图中
k.create_curve(ma5, "white", offset=5, price=True)
k.create_curve(ma10, "blue", offset=10, price=True)
k.create_curve(ma30, "purple", offset=30, price=True)

# 绘制k线图并以展示出来
k.draw()