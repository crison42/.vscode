# 定义货物结构体，包含重量和价值
class Cargo:
    def __init__(self, weight, value):
        self.weight = weight  # 货物重量
        self.value = value  # 货物价值


# 最优装载的贪心算法
def optimal_loading(cargoes, capacity):
    # 按照货物重量进行非递增排序
    cargoes.sort(key=lambda x: x.weight, reverse=True)
    loaded_cargoes = []
    current_load = 0

    for cargo in cargoes:
        if current_load + cargo.weight <= capacity:
            loaded_cargoes.append(cargo)
            current_load += cargo.weight

    return loaded_cargoes, current_load


# 测试数据
cargoes = [Cargo(10, 5), Cargo(20, 10), Cargo(30, 15), Cargo(40, 20), Cargo(50, 25)]
capacity = 70

# 调用最优装载的贪心算法
loaded_cargoes, current_load = optimal_loading(cargoes, capacity)

# 输出结果
print("已装载货物列表:")
for cargo in loaded_cargoes:
    print("重量:", cargo.weight, " 价值:", cargo.value)
print("当前装载重量:", current_load)
