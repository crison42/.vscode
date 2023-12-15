# 定义一个函数 recur_matrix_chain，用于计算矩阵链乘法问题的最优解
# 参数 i 和 j 分别表示矩阵链的起始和结束位置，s 是一个二维列表，用于存储子问题的解，p 是一个列表，表示矩阵链中各个矩阵的大小
def recur_matrix_chain(i, j, s, p):
   # 如果 i 和 j 相等，说明矩阵链中只有一个矩阵，返回 0
   if i == j:
       return 0
   # 计算子问题 recur_matrix_chain(i, i) + recur_matrix_chain(i + 1, j) + p[i - 1] * p[i] * p[j] 的最小值
   u = (
       recur_matrix_chain(i, i, s, p)
       + recur_matrix_chain(i + 1, j, s, p)
       + p[i - 1] * p[i] * p[j]
   )
   # 将 s[i][j] 更新为使 u 最小的 k
   s[i][j] = i
   for k in range(i + 1, j):
       # 计算子问题 recur_matrix_chain(i, k) + recur_matrix_chain(k + 1, j) + p[i - 1] * p[k] * p[j] 的最小值
       t = (
           recur_matrix_chain(i, k, s, p)
           + recur_matrix_chain(k + 1, j, s, p)
           + p[i - 1] * p[k] * p[j]
       )
       # 如果 t < u，则更新 u 和 s[i][j]
       if t < u:
           u = t
           s[i][j] = k
   # 返回 u，即矩阵链乘法问题的最优解
   return u


# 定义一个函数 traceback，用于回溯矩阵链的最优计算次序
# 参数 i 和 j 分别表示矩阵链的起始和结束位置，s 是一个二维列表，用于存储子问题的解
def traceback(i, j, s):
   # 如果 i 和 j 相等，说明矩阵链中只有一个矩阵，不需要进行回溯
   if i == j:
       return
   # 回溯子问题 recur_matrix_chain(i, s[i][j])
   traceback(i, s[i][j], s)
   # 回溯子问题 recur_matrix_chain(s[i][j] + 1, j)
   traceback(s[i][j] + 1, j, s)
   # 打印矩阵链的计算次序
   print(f"Multiply A{i},{s[i][j]} and A{s[i][j] + 1},{j}")


# 主函数 main，用于调用 recur_matrix_chain 和 traceback 函数，计算矩阵链的最少计算次数和最优计算次序
def main():
   # 定义矩阵链中矩阵的大小
   p = [30, 35, 15, 5, 10, 20, 25]
   # 计算矩阵链的长度
   L = len(p)
   # 初始化二维列表 s，用于存储子问题的解
   s = [[0] * L for _ in range(L)]
   # 计算矩阵链的最少计算次数
   min_operations = recur_matrix_chain(1, L - 1, s, p)
   print("矩阵的最少计算次数为：", min_operations)
   # 打印矩阵链的最优计算次序
   print("矩阵最优计算次序为：")
   # 回溯矩阵链的最优计算次序
   traceback(1, L - 1, s)


# 调用主函数 main
if __name__ == "__main__":
   main()
