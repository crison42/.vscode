import random

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return color_code

# 生成随机颜色代码并打印
random_color = generate_random_color()
print(random_color)