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
length=float(input("Please enter length: "))
line_color=input("Please enter line color: ")
draw_square(length,line_color)
