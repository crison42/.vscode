# x为超量怪兽星级，y为融合怪兽星级，a为双方手牌场上卡牌数量之和，b为所选怪兽星级
for b in range(2, 13):
    a_list = []
    x = (b - 1) / 1
    y = float(1)
    if x.is_integer() and y.is_integer() and x >= 0 and y > 0:
        a = 2 * int(x) + int(y)
        if a not in a_list:
            a_list.append(a)

    x = float(1)
    y = float(b)
    if x.is_integer() and y.is_integer() and x > 0 and y > 0:
        a = 2 * int(x) + int(y)
        if a not in a_list:
            a_list.append(a)

    for a in a_list:
        a = float(a)
        if a.is_integer() and a >= 1:
            print(
                f"当 b = {b} 时, 存在解: x = {int(a - b)}, y = {int(b - (a - b))}, a = {int(a)}"
            )
