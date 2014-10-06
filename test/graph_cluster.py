__author__ = 'ict'

import DAL.yahoo  # 读取yahoo股票数据
import calculate.generator  # 关系网络图生成器
import calculate.cluster.graph.core  # 聚类模块
import calculate.helper.modularity  # 模块化指标计算函数
import interface.console.print_cluster  # 聚类结果输出函数
import calculate.helper.threshold  # 阈值化处理的相关函数

# 读取存放在e盘下的yahoo股票数据，使用数据中的复权值（adjclose）。
data = DAL.yahoo.csv(r"e:\stockdata", "adjclose")

# 使用生成器以“price return”为特征，用余弦（cos）相似度进行网络构建。
g = calculate.generator.graph_relation(data, "price return", "cos")

# 按照0.75的下限阈值和0.99的上限阈值进行处理
calculate.helper.threshold.edge_thr(g, 0.75)
calculate.helper.threshold.edge_thr(g, 0.99, reverse=True)

# 用完全图聚类的方法进行图聚类
cls = calculate.cluster.graph.core.method("complete graph", g)

# 计算并显示聚类后的模块化指标
print(calculate.helper.modularity.value_q(g, cls))

# 打印输出聚类的结果
interface.console.print_cluster.print_cluster(cls)