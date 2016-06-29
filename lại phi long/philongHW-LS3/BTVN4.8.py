from turtle import *

##speed()
def draw_star(x,y,a):
    penup()
    setpos (x,y)
    pendown()
    for i in range (5):
        
        forward(a)
        left (144)
x= int(input('Nhap hoanh do: '))
y= int(input('Nhap tung do: '))
a= int(input('Nhap chieu dai: '))
draw_star(x,y,a)
speed(0)
color('blue')
for i in range(100):
 import random
 x = random.randint(-300, 300)
 y = random.randint(-300, 300)
 length = random.randint(3, 10)
 draw_star(x, y, length)


