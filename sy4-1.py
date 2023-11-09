# 商品库存
inventory = {}

# 操作菜单
menu = [
   "1.查询商品",
   "2.新增商品",
   "3.卖出商品",
   "4.汇总",
   "-1.退出系统"
]

# 查询商品
def query_product():
   if not inventory:
       print("当前库存商品为零")
   else:
       for product, info in inventory.items():
           print(f"{product}: 进货价格 {info['in_price']}, 销售价格 {info['sale_price']}, 库存数量 {info['stock']}")

# 新增商品
def add_product():
   product = input("请输入商品名称：")
   in_price = float(input("请输入进货价格："))
   sale_price = float(input("请输入销售价格："))
   stock = int(input("请输入进货数量："))
   inventory[product] = {
       "in_price": in_price,
       "sale_price": sale_price,
       "stock": stock
   }
   print(f"成功添加商品 {product}")

# 卖出商品
def sell_product():
   product = input("请输入商品名称：")
   if product not in inventory:
       print("商品不存在")
   else:
       stock = inventory[product]["stock"]
       sale_num = int(input("请输入销售数量："))
       if stock >= sale_num:
           inventory[product]["stock"] -= sale_num
           print(f"成功卖出商品 {product}，库存数量 {stock - sale_num}")
           total_in_price = sum([info["in_price"] * stock for product, info in inventory.items()])
           total_sale_price = sum([info["sale_price"] * stock for product, info in inventory.items()])
           print(f"进货总货款 {total_in_price}, 总销售额 {total_sale_price}")
       else:
           print("库存数量不足")

# 汇总
def summary():
   if not inventory:
       print("当前库存商品为零")
   else:
       for product, info in inventory.items():
           print(f"{product}: 进货价格 {info['in_price']}, 销售价格 {info['sale_price']}, 库存数量 {info['stock']}")
       total_in_price = sum([info["in_price"] * stock for product, info in inventory.items()])
       total_sale_price = sum([info["sale_price"] * stock for product, info in inventory.items()])
       print(f"进货总货款 {total_in_price}, 总销售额 {total_sale_price}")

# 主程序
while True:
   print("******欢迎使用超市管理系统**********")
   for i, operation in enumerate(menu):
       print(f"{i + 1}. {operation}")
   choice = int(input("请输入操作序号："))
   if choice == 1:
       query_product()
   elif choice == 2:
       add_product()
   elif choice == 3:
       sell_product()
   elif choice == 4:
       summary()
   elif choice == -1:
       print("退出系统")
       break
   else:
       print("无效的操作序号，请重新输入")