def draw_square(d,y):
    color(y)
    for i in range(4):
        fd(d)
        left(360/4)
y = str(input('Enter the color: '))
d = int(input('Enter the length: '))
from turtle import*
draw_square(d,y)
        
