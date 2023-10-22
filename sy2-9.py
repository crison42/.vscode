print("商品列表\n编号\t名称")
products = [
    {"wealth": 1, "name": "冰露纯净水"},
    {"wealth": 2, "name": "农夫山泉"},
    {"wealth": 3, "name": "柠檬绿茶"},
    {"wealth": 3, "name": "冰红茶"},
    {"wealth": 3, "name": "茉莉花茶"},
    {"wealth": 4, "name": "脉动"},
    {"wealth": 5, "name": "红牛"},
    ]
for i in range(len(products)):
    print("{0}\t{1}".format(i,products[i]["name"]))
num=input("请输入购买的商品编号")
num=int(num)
if num<0 or num>len(products):
    print("商品不存在")
else:
    print("付款金额{0}元".format(products[num]["wealth"]))
    figure=input("请输入付款金额")
    figure=int(figure)
    while figure!=products[num]["wealth"]:
        print("付款失败,请重新付款")
        figure=input("请输入付款金额")
        figure=int(figure)
    print("购买成功")