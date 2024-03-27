import numpy as np
from sklearn.linear_model import LinearRegression

# 创建数据集
x = np.array([80, 82, 85, 90, 86, 82, 78])  # 平时成绩
y = np.array([86, 80, 78, 90, 82, 90, 80])  # 期末成绩
z= np.array([84.2,80.6,80.1,90,83.2,87.6,79.4])# 最终成绩

# 创建二元线性回归模型
model = LinearRegression()

# 预测最终成绩
model.fit(np.array([x, y]).T, z)

# 输出模型系数
print("平时成绩权重:{:.2f}".format(model.coef_[0]))
print("期末成绩权重:{:.2f}".format(model.coef_[1]))

# 输出预测成绩
print("预测最终成绩:", model.predict([[83, 85]]))