import torch
from torchviz import make_dot

# 构建模型
model = torch.load("model/murasame.pth")  # 在这里定义你的模型

# 创建一个示例输入
example_input = torch.randn(1, 3, 224, 224)

# 将模型和示例输入传递给make_dot函数
graph = make_dot(model(example_input), params=dict(model.named_parameters()))

# 保存图形为PDF文件
graph.format = 'pdf'
graph.render("model_graph")