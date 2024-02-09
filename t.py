import turtle
import random

def draw_fu(text, font, color, bg_color):
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.color(color)
    turtle.bgcolor(bg_color)
    turtle.write(text, align='center', font=(font, 100, 'normal'))
    turtle.hideturtle()
    turtle.done()

def generate_random_fu():
    font_list = ['Arial', 'Times New Roman', 'Courier', 'Verdana']
    color_list = ['red', 'blue', 'green', 'purple', 'orange']
    bg_color_list = ['white', 'gray', 'yellow', 'lightblue', 'lightgreen']
    
    random_font = random.choice(font_list)
    random_color = random.choice(color_list)
    random_bg_color = random.choice(bg_color_list)
    
    draw_fu('福', random_font, random_color, random_bg_color)

generate_random_fu()