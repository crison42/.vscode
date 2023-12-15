import numpy as np

# 定义一个函数 knapsack，用于计算背包问题中的最大价值
# 参数 w 是一个列表，表示物品的重量
# 参数 v 是一个列表，表示物品的价值
# 参数 W 是一个整数，表示背包的容量
def knapsack(w, v, W):
   # 添加一个物品，重量为0，价值为0，表示不选择任何物品
   w.insert(0, 0)
   v.insert(0, 0)
   # 物品的数量
   n = len(w)
   # 创建一个二维数组 c，用于存储子问题的解
   c = np.zeros((n, W + 1), dtype=np.int32)
   # 动态规划求解子问题
   for i in range(1, n):
       for j in range(1, W + 1):
           if w[i] <= j:
               c[i][j] = max(c[i - 1][j - w[i]] + v[i], c[i - 1][j])
           else:
               c[i][j] = c[i - 1][j]
   # 记录背包中所装物品
   x = [0 for _ in range(n)]
   # 逆向寻找物品
   j = W
   for i in range(n - 1, 0, -1):
       if c[i][j] > c[i - 1][j]:
           x[i - 1] = 1
           j -= w[i - 1]
   # 返回最大价值和背包中所装物品
   return c[n - 1][W], x

# 主函数，用于调用 knapsack 函数，计算背包问题中的最大价值和所装物品
if __name__ == "__main__":
   # 物品的重量
   w = [2, 2, 6, 5, 4]
   # 物品的价值
   v = [3, 6, 5, 4, 6]
   # 背包的容量
   w_most = 10
   # 计算最大价值和所装物品
   bestp, x = knapsack(w, v, w_most)
   # 输出最大价值和所装物品
   print('最大价值为：', bestp)
   print('背包中所装物品为:', x)
