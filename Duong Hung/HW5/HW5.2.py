from turtle import*
def draw_square(d1,d2):
    color(d2)
    for i in range(4):
        forward(d1)
        left(360/4)

for i in range(30):
    draw_square(i*5, 'Red')
    left(17)
    penup()
    forward(i*2)
    pendown()
