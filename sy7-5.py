while True:
    try:
        # 获取用户输入
        data = input("输入0-4会发生异常")

        # 尝试将输入的字符串转换为整数
        num = int(data)

        # 如果转换失败，则捕获TypeError异常
        if not isinstance(num, int):
            raise ValueError("输入的数据不是整数")

        if num == 0:
            
            raise ZeroDivisionError("0不能作除数")

        if num == 1:
            alist = [1,2,3]
            print(alist[4])
            raise IndexError("下标越界了")

        if num == 2:
            raise TypeError("字符串和整数不能相加")

        if num == 3:
            raise FileNotFoundError("你导入的模块不存在")

        if num == 4:
            raise NameError("变量名未定义")

        if num == 5:
            raise AttributeError("欢迎来到没有异常的分支")

    except Exception as e:
        print(e)
    else:
        print("输入的不是0-4,没有发生异常")
        break
