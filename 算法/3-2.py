import numpy as np
def knapsack(w,v,W):#return max v
    w.insert(0,0)#前0件要用
    v.insert(0,0)#前0件要用
    n = len(w)
    c=np.zeros((n,W+1),dtype=np.int32)#下标从零开始
    for i in range(1,n):
        for j in range(1,W+1):
            if w[i]<=j:
                c[i][j]=max(c[i-1][j-w[i]]+v[i],c[i-1][j])
            else:
                c[i][j]=c[i-1][j]
    x = [0 for i in range(n)]
    j = W
    for i in range(n-1, 0, -1):
        if c[i][j] > c[i - 1][j]:
            x[i - 1] = 1
            j -=  w[i - 1]
    return c[n-1][W],x

if __name__ =="__main__":
    w =[2,2,6,5,4]
    v = [3,6,5,4,6]
    w_most = 10
    bestp,x =knapsack(w,v,w_most)
    print('最大价值为：',bestp)
print('背包中所装物品为:',x) 