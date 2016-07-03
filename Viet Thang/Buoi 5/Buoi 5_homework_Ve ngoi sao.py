#Ve ngoi sao

from turtle import *

def draw_star(x,y,length):
    penup()
    x=setx(x)
    y=sety(y)
    pendown()

    left(36)
    for i in range(5):
        forward(length)
        left(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    length = random.randint(3,10)
    draw_star(x,y,length)
