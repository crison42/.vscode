import matplotlib.pyplot as plt

# 样本数据
x = [6, 8, 10, 14, 18]
y = [7, 11, 13, 17.5, 18]

# 计算斜率和截距
n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum([a * b for a, b in zip(x, y)])  # 修正这里
sum_x2 = sum([a ** 2 for a in x])

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - a * sum_x) / n

# 绘制样本数据
plt.scatter(x, y, label='Sample Data')

# 绘制模型
x_model = range(6, 19)
y_model = [a * x + b for x in x_model]
plt.plot(x_model, y_model, label='Model')

# 设置图表标题和坐标轴标签
plt.title('The relationship between pizza price and diameter')
plt.xlabel('diameter (inch)')
plt.ylabel('Price (USD)')

# 显示图例
plt.legend()

# 显示图形
plt.show()

k=input()
print(k*a+b)