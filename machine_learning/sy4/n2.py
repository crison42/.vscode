import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import r2_score

# 加载数据集
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
data = pd.read_csv(url, names=columns)

# 数据预处理
data = pd.get_dummies(data, columns=['Sex'])  # 对性别进行独热编码
X = data.drop('Rings', axis=1)
y = data['Rings']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 特征缩放
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 调整SVM参数并评估模型性能
gamma_values = [0.1, 1, 10]
C_values = [0.1, 1, 10]

for gamma in gamma_values:
    for C in C_values:
        svr = SVR(kernel='rbf', gamma=gamma, C=C)
        svr.fit(X_train_scaled, y_train)
        y_pred = svr.predict(X_test_scaled)
        r2 = r2_score(y_test, y_pred)
        print(f"Gamma={gamma}, C={C}, R^2 score: {r2}")