from turtle import*
shape('turtle')
speed(0)
def draw_square(a,b):
    for x in range(4):
        color(b,"white")
        begin_fill()
        forward(a)
        left(90)
        end_fill()
for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
