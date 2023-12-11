import random

# 随机生成一个长度为100的整数列表
nums = [random.randint(1, 100) for _ in range(100)]

# 计算和及平均值
sum_value = sum(nums)
avg_value = sum_value / len(nums)

# 排序后将和及平均值追加到列表的末尾
nums=sorted(nums)
nums.append(sum_value)
nums.append(avg_value)

# 输出列表
flag=0
for i in nums:
    print(i, end=" ")
    flag+=1
    if(flag%10==0):
        print()

# 将列表以每行10个(元素之间以空格分隔)写入一个文本文件
with open("软工XX班张三3.txt", "w") as f:
    for i in range(0, len(nums), 10):
        f.write(" ".join(map(str, nums[i : i + 10])) + "\n")
