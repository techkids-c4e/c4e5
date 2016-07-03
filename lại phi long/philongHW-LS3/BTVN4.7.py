from turtle import*   
def draw_square(a,b):
    color (b)
    begin_fill()
    for x in range (4):
        forward(a)
        left (90)
    end_fill()
a= int(input('What is the length of the square?: '))
b= input('What color is the square?: ')
draw_square(a,b)
for i in range(30):
 draw_square(i * 5, 'red')
 left(17)
 penup()
 forward(i * 2)
 pendown()
