__author__ = 'ict'

from calculate.classify.DT import DT

# 数据组
data = [
    ["Sunny", "Hot", "High", "Weak"],
    ["Sunny", "Hot", "High", "Strong"],
    ["Overcast", "Hot", "High", "Weak"],
    ["Rain", "Mild", "High", "Weak"],
    ["Rain", "Cool", "Normal", "Weak"],
    ["Rain", "Cool", "Normal", "Strong"],
    ["Overcast", "Cool", "Normal", "Strong"],
    ["Sunny", "Mild", "High", "Weak"],
    ["Sunny", "Cool", "Normal", "Weak"],
    ["Rain", "Mild", "Normal", "Weak"],
    ["Sunny", "Mild", "Normal", "Strong"],
    ["Overcast", "Mild", "High", "Strong"],
    ["Overcast", "Hot", "Normal", "Weak"],
    ["Rain", "Mild", "High", "Strong"]
]

# 标签组
label = ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]

# 创建决策树分类器
dt = DT()

# 训练分类器
dt.train(data, label)

# 打印决策树形态
print(dt.tree)

# 测试分类器对训练样本的分类
print(dt.classify(data))

# 保存分类器
dt.save(r"e:\dt.ict")

# 创建一个新的决策树分类器
new_dt = DT()

# 载入之前保存的分类器
new_dt.load(r"e:\dt.ict")

# 测试新分类器是否和之前结果一样
print(dt.classify(data))