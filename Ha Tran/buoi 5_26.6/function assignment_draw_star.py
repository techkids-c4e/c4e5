from turtle import*
def draw_star(x,y,length):
    penup()
    x=setx(x)
    y=sety(y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
draw_star(-100,0,200)
    
speed(0)
color('blue')
for i in range(100):
     import random

     x = random.randint(-300, 300)
     y = random.randint(-300, 300)
     length = random.randint(3, 10)
     draw_star(x, y, length)
