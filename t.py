import turtle
import random
import matplotlib.font_manager as fm


def draw_fu(text, font, color, bg_color):
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.color(color)
    turtle.bgcolor(bg_color)
    turtle.write(text, align="center", font=(font, 100, "normal"))
    turtle.hideturtle()
    turtle.done()


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return color_code


def generate_random_font():
    available_fonts = fm.findSystemFonts()
    random_font = random.choice(available_fonts)
    return random_font


def generate_random_fu():

    random_font = generate_random_font()
    random_color = "#b6ccfb"
    random_bg_color = "#d6b6fb"

    draw_fu("福", random_font, random_color, random_bg_color)


generate_random_fu()
