while True:
    try:
        # 获取用户输入
        data = input("输入0-4会发生异常")

        # 尝试将输入的字符串转换为整数
        num = int(data)

        if num == 0:
            raise ZeroDivisionError("0不能作除数")

        if num == 1:
            raise IndexError("下标越界了")

        if num == 2:
            raise TypeError("字符串和整数不能相加")

        if num == 3:
            raise FileNotFoundError("你导入的模块不存在")

        if num == 4:
            raise NameError("变量名未定义")

        if num == 5:
            raise AttributeError("欢迎来到没有异常的分支")

    except ValueError:
        print("输入的不是0-4,没有发生异常")
        break
    except Exception as e:
        print(e)
    else:
        print("输入的不是0-4,没有发生异常")
        break
