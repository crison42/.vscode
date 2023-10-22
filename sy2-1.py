count = 0  # 用于计数满足条件的3位数的个数

# 外层循环选择百位数字
for i in range(1, 5):
    # 内层循环选择十位和个位数字
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (i != k):
                # 组合数字并打印
                num = i * 100 + j * 10 + k
                count += 1

print("共有{0}个".format(count) )