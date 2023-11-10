# 商品库存
inventory = {}

# 总销售额/总进货额(可变更全局变量)
total_sale_price = 0
total_in_price = 0

# 操作菜单
menu = ["1.查询商品", "2.新增商品", "3.卖出商品", "4.汇总", "-1.退出系统"]


# 查询商品
def query_product():
    if not inventory:
        print("当前库存商品为零")
    else:
        for product, info in inventory.items():
            print(
                f"商品名称:{product},进货价格{info['in_price']},销售价格:{info['sale_price']},库存数量:{info['stock']}"
            )


# 新增商品
def add_product():
    global total_in_price  # 全局变量标记
    product = input("请输入商品名称:")
    in_price = input("请输入进货价格:")
    sale_price = input("请输入销售价格:")
    stock = input("请输入进货数量:")
    if int(in_price) <= 0 or int(sale_price) <= 0 or int(stock) < 0:
        print("价格必须大于0,数量必须为非负数")
    elif in_price.isdigit() and sale_price.isdigit() and stock.isdigit():
        inventory[product] = {
            "in_price": int(in_price),
            "sale_price": int(sale_price),
            "stock": int(stock),
        }
        if stock > 0:
            total_in_price += in_price * stock
    else:
        print("输入数值必须为数字")


# 卖出商品
def sell_product():
    global total_sale_price  # 全局变量标记
    product = input("请输入商品名称:")
    if product not in inventory:
        print("商品不存在")
    else:
        stock = inventory[product]["stock"]
        sale_num = int(input("请输入销售数量:"))
        if str(sale_num).isdigit(): # 数字判定
            if stock >= sale_num:
                price = int(inventory[product]["sale_price"] * sale_num)
                print(f"应付款={price}")
                pay = int(input("请输入付款金额:"))
                if str(pay).isdigit():# 数字判定
                    if pay >= price:
                        inventory[product]["stock"] -= sale_num
                        print(f"找零={pay-price}")
                        total_sale_price += price
                    else:
                        print("付款金额不足")
                else:
                    print("输入数值必须为数字")
            else:
                print("库存数量不足")
        else:
            print("输入数值必须为数字")


# 汇总
def summary():
    global total_sale_price, total_in_price  # 全局变量标记
    if not inventory:
        print("当前库存商品为零")
    else:
        print("超市现有商品情况")
        print("商品名称        进货价格        销售价格        库存数量")
        for product, info in inventory.items():
            print(
                f"{product.ljust(14)}{str(info['in_price']).ljust(16)}{str(info['sale_price']).ljust(16)}{str(info['stock']).ljust(16)}"
            )
        print(f"总销售额:{total_sale_price}" + "\n" + f"总进货额:-{total_in_price}")


# 主程序
print("***********欢迎进入超市管理系统************")
for index, item in enumerate(menu, start=1):
    print(f"{item}")
while True:
    choice = int(input("******请输入菜单编号:"))
    if choice == 1:
        query_product()
    elif choice == 2:
        add_product()
    elif choice == 3:
        sell_product()
    elif choice == 4:
        summary()
    elif choice == -1:
        print("谢谢使用")
        break
    else:
        print("无效的操作序号，请重新输入")
