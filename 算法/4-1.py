# 定义一个函数 knapsack，用于解决背包问题
# 参数 items 是一个物品列表，每个物品是一个元组，包含重量和价值
# 参数 max_weight 是背包的最大承重
def knapsack(items, max_weight):
    # 初始化最大价值为0
    max_value = [0]

    # 定义一个回溯函数 backtrack
    def backtrack(i, cw, cv):
        # 如果当前物品的重量超过背包的最大承重，或者已经遍历完所有物品，返回
        if cw > max_weight or i == len(items):
            if cv > max_value[0]:
                max_value[0] = cv
            return
        # 不选当前物品，继续遍历下一个物品
        backtrack(i + 1, cw, cv)
        # 如果当前物品的重量加上背包的剩余承重小于等于背包的最大承重，选择当前物品，继续遍历下一个物品
        if cw + items[i][0] <= max_weight:
            backtrack(i + 1, cw + items[i][0], cv + items[i][1])

    # 调用回溯函数，从第一个物品开始遍历
    backtrack(0, 0, 0)

    # 返回最大价值
    return max_value[0]


# 定义物品列表
items = [(2, 3), (3, 4), (4, 5), (5, 8)]
# 定义背包的最大承重
max_weight = 10
# 调用 knapsack 函数，计算最大价值
print("最大价值为:", knapsack(items, max_weight))
