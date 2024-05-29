import matplotlib.pyplot as plt
import numpy as np

# 定义一个函数生成嵌套的圆环数据
def generate_nested_circles(n_points, noise=0.05):
    # 内圆环
    circle1 = np.random.rand(n_points // 2, 2) * 0.5 + 0.25
    # 外圆环
    circle2 = np.random.rand(n_points // 2, 2) * 0.5 + 0.75
    # 噪声点
    noise_points = np.random.rand(int(n_points * noise), 2) * 2 - 1
    # 合并数据集
    data = np.vstack((circle1, circle2, noise_points))
    return data

# 生成数据集
data = generate_nested_circles(100)

# 可视化数据集
plt.scatter(data[:, 0], data[:, 1])
plt.show()

from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

# 使用DBSCAN进行聚类
model = DBSCAN()
clusters = model.fit_predict(data)

# 可视化聚类结果
plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='viridis')
plt.show()
# 调整参数
eps_values = [0.1, 0.2, 0.3, 0.4, 0.5]
min_samples_values = [5, 10, 15, 20, 25]

# 寻找最佳参数
best_score = 0
best_params = {'eps': 0, 'min_samples': 0}
for eps in eps_values:
    for min_samples in min_samples_values:
        model = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = model.fit_predict(data)
        score = silhouette_score(data, clusters)  # 使用轮廓系数评估聚类效果
        if score > best_score:
            best_score = score
            best_params['eps'] = eps
            best_params['min_samples'] = min_samples

print("最佳参数：", best_params)
