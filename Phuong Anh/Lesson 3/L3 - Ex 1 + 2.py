from turtle import*
def draw_square(length,color): #dinh nghia ham draw_square
    pencolor(color) #line colour
    for i in range (4): #ve hinh vuong
        forward(length)
        left(90)
    
for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
