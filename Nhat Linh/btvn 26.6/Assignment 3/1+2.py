from turtle import*
l=int(input('length'))
c=input('color')
def draw_square(l,c):
    color(c)
    for x in range(4):
        forward(l)
        left(360/4)
draw_square(l,c)

for i in range(30):
 draw_square(i * 5, 'red')
 left(17)
 penup()
 forward(i * 2)
 pendown()
