import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# 加载数据集
iris = datasets.load_iris()
X = iris.data[:, :2]  # 选择前两个特征
y = iris.target

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建支持向量机对象
svc = SVC(kernel='linear', C=1)

# 训练模型
svc.fit(X_train, y_train)

# 进行预测
y_pred = svc.predict(X_test)

# 计算准确率
accuracy = svc.score(X_test, y_test)

print("准确性:", accuracy)