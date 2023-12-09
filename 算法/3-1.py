# # A1 30*35 A2 35*15 A3 15*5 A4 5*10 A5 10*20 A6 20*25
# # p[0-6]={30,35,15,5,10,20,25}

# L = 7

# def recur_matrix_chain(i, j, s, p):
#     if i == j:
#         return 0
#     u = recur_matrix_chain(i, i, s, p) + recur_matrix_chain(i + 1, j, s, p) + p[i - 1] * p[i] * p[j]
#     s[i][j] = i

#     for k in range(i + 1, j):
#         t = recur_matrix_chain(i, k, s, p) + recur_matrix_chain(k + 1, j, s, p) + p[i - 1] * p[k] * p[j]
#         if t < u:
#             u = t
#             s[i][j] = k
#     return u

# def traceback(i, j, s):
#     if i == j:
#         return
#     traceback(i, s[i][j], s)
#     traceback(s[i][j] + 1, j, s)
#     print("Multiply A{} and A{}".format(i, s[i][j]))
#     print("Multiply A{} and A{}".format(s[i][j] + 1, j))


# p = [30, 35, 15, 5, 10, 20, 25]
# s = [[0 for i in range(L)] for j in range(L)]
# print(recur_matrix_chain(1, 6, s, p))
# traceback(1, 6, s)
def recur_matrix_chain(i, j, s, p):
    if i == j:
        return 0
    u = (
        recur_matrix_chain(i, i, s, p)
        + recur_matrix_chain(i + 1, j, s, p)
        + p[i - 1] * p[i] * p[j]
    )
    s[i][j] = i

    for k in range(i + 1, j):
        t = (
            recur_matrix_chain(i, k, s, p)
            + recur_matrix_chain(k + 1, j, s, p)
            + p[i - 1] * p[k] * p[j]
        )
        if t < u:
            u = t
            s[i][j] = k
    return u


def traceback(i, j, s):
    if i == j:
        return
    traceback(i, s[i][j], s)
    traceback(s[i][j] + 1, j, s)
    print(f"Multiply A{i},{s[i][j]} and A{s[i][j] + 1},{j}")


def main():
    p = [30, 35, 15, 5, 10, 20, 25]
    L = len(p)
    s = [[0] * L for _ in range(L)]
    print("矩阵的最少计算次数为：", recur_matrix_chain(1, L - 1, s, p))
    print("矩阵最优计算次序为：")
    traceback(1, L - 1, s)


if __name__ == "__main__":
    main()
