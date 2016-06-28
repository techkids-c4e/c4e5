from turtle import*
import math
def draw_star(x,y,length):
    penup()
    setpos(x,y)
    left(90)
    i=length/(2*math.sin(72*math.pi/180))
    forward(i)
    pendown()
    left(180-36/2)
    for i in range(5):
        forward(length)
        left(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    length=random.randint(3, 10)
    draw_star(x,y,length)


            
