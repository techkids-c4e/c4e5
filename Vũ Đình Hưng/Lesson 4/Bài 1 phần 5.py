from turtle import *
speed(0)
def draw_square(x, y):
    color(y)
    for a in range (4):
        forward(x)
        left(90)
square_length = float(input('What is the length of the square?: '))
square_color = input('What is the color of the square?: ')
draw_square(square_length, square_color)
