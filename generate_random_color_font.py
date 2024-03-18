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

import matplotlib.font_manager as fm

def generate_random_font():
    available_fonts = fm.findSystemFonts()
    random_font = random.choice(available_fonts)
    return random_font

# 生成随机字体并打印
random_font = generate_random_font()
print(random_font)