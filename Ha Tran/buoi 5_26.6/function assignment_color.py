from turtle import*
speed(0)
shape('turtle')
color=color('red')
def draw_square(length,color):
    for x in range(4):
        forward(length)
        left(90)
for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
