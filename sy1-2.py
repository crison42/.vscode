def NextDate(Y, M, D):
    # 检查输入的年、月、日是否合法
    if Y <= 0 or M <= 0 or M > 12 or D <= 0:
        return "无效日期"

    # 检查是否是闰年
    is_leap_year = False
    if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
        is_leap_year = True

    # 检查月份的天数是否合法
    if (M == 2 and is_leap_year and D > 29) or (M == 2 and not is_leap_year and D > 28):
        return "无效日期"
    elif ((M == 4 or M == 6 or M == 9 or M == 11) and D > 30) or (D > 31):
        return "无效日期"

    # 计算下一天的日期
    if (M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10):
        if D == 31:
            return str(Y) + "-" + str(M+1) + "-1"
        else:
            return str(Y) + "-" + str(M) + "-" + str(D+1)
    elif M == 12:
        if D == 31:
            return str(Y+1) + "-1-1"
        else:
            return str(Y) + "-" + str(M) + "-" + str(D+1)
    elif M == 2:
        if is_leap_year:
            if D == 29:
                return str(Y) + "-3-1"
            else:
                return str(Y) + "-" + str(M) + "-" + str(D+1)
        else:
            if D == 28:
                return str(Y) + "-3-1"
            else:
                return str(Y) + "-" + str(M) + "-" + str(D+1)
    else:
        if D == 30:
            return str(Y) + "-" + str(M+1) + "-1"
        else:
            return str(Y) + "-" + str(M) + "-" + str(D+1)

input = input("请输入日期（格式：yyyy-mm-dd）：")
# input = "2022-12-31"
# input = "2023-2-28"
# input = "0-5-10"
# input = "2023-0-4"
# input = "2023-8-0"
# input = "2023-2-29"
# input = "2023-4-31"
# input = "2023-5-32"
Y, M, D = input.split("-")
Y = int(Y)
M = int(M) 
D = int(D)
NextDate = NextDate(Y, M, D)
print("下一天是"+str(NextDate))