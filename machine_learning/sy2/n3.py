import numpy as np
from sklearn.datasets import fetch_california_housing, fetch_openml
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error

# 加载加利福尼亚房价数据集
housing = fetch_california_housing()
X = housing.data
y = housing.target

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建岭回归模型
ridge = Ridge()

# 使用交叉验证对模型进行评估
scores = cross_val_score(ridge, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
print("岭回归交叉验证均方误差:", -scores.mean())

# 使用测试集对模型进行预测
ridge.fit(X_train, y_train)
y_pred = ridge.predict(X_test)

# 计算均方误差
mse = mean_squared_error(y_test, y_pred)
print("岭回归测试集均方误差:", mse)

# 创建套索回归模型
lasso = Lasso()

# 使用交叉验证对模型进行评估
scores = cross_val_score(lasso, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
print("套索回归交叉验证均方误差:", -scores.mean())

# 使用测试集对模型进行预测
lasso.fit(X_train, y_train)
y_pred = lasso.predict(X_test)

# 计算均方误差
mse = mean_squared_error(y_test, y_pred)
print("套索回归测试集均方误差:", mse)
