import numpy as np

def solve_linear_equations(coefficients, constants):
    A = np.array(coefficients)
    b = np.array(constants)
    
    # 检查矩阵A是否可逆
    if np.linalg.det(A) == 0:
        return "方程组无解或有无穷多解"
    
    # 使用线性方程组的求解公式求解
    x = np.linalg.solve(A, b)
    return x

# 示例输入
coefficients = [[1, 2, 3], [0, 4, 5], [0, 0, 6]]#对应x1,x2,x3系数
constants = [6, 9, 12]#对应右侧系数

# 求解线性方程组
solution = solve_linear_equations(coefficients, constants)

# 打印结果
print(solution)