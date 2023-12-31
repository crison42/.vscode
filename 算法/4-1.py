# 定义一个函数knapsack，接收两个参数：物品列表items和背包的最大承重max_weight
def knapsack(items, max_weight):
   # 定义一个内部函数backtrack，接收三个参数：当前物品索引i、当前背包的重量cw和当前背包的价值cv
   def backtrack(i, cw, cv):
       # 如果当前背包的重量超过最大承重，或者已经遍历完所有物品，则返回
       if cw > max_weight or i == len(items):
           # 如果当前背包的价值大于已记录的最大价值，则更新最大价值
           if cv > max_value:
               max_value = cv
           return
       # 不选当前物品，继续递归遍历下一个物品
       backtrack(i + 1, cw, cv)
       # 如果当前背包的重量加上当前物品的重量不超过最大承重，则选当前物品，继续递归遍历下一个物品
       if cw + items[i][0] <= max_weight:
           backtrack(i + 1, cw + items[i][0], cv + items[i][1])

   # 初始化最大价值为0
   max_value = 0
   # 开始递归遍历
   backtrack(0, 0, 0)
   # 返回最大价值
   return max_value

# 定义物品列表items，格式为(重量, 价值)
items = [(2, 3), (3, 4), (4, 5), (5, 8)]
# 定义背包的最大承重max_weight
max_weight = 10
# 调用knapsack函数，并打印最大价值
print("Maximum value in knapsack:", knapsack(items, max_weight))
