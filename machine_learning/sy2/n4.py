import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data
y = iris.target

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建逻辑回归模型
log_reg = LogisticRegression(max_iter=1000)

# 使用交叉验证对模型进行评估
scores = cross_val_score(log_reg, X_train, y_train, cv=5, scoring='accuracy')
print("交叉验证准确率:", scores.mean())

# 使用测试集对模型进行预测
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("测试集准确率:", accuracy)
