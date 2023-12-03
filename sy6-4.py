import random
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.family"] = "SimHei"

# 学生人数和分数数据
students = ["优秀", "良好", "中等", "及格", "不及格"]
scores = [49, 41, 16, 5, 2]

# 生成随机颜色编号
colors = [
    "#" + "".join(random.choices("0123456789ABCDEF", k=6)) for _ in range(len(students))
]

# 绘制柱状图
plt.bar(students, scores, color=colors)

# 添加标题和标签
plt.title("成绩分布柱形图")
plt.xlabel("人数")
plt.ylabel("成绩等级")

# 显示图形
plt.show()
