from turtle import*
shape('turtle')
speed(0)
def draw_star(x,y,length):
    penup()
    forward(x)
    left(90)
    forward(y)
    right(90)
    pendown()      
    for a in range(5):
        forward(length)
        right(144)
x=float(input('Please enter x for the location of the star: '))
y=float(input('Please enter y for the location of the star: '))
length=float(input('Please enter length of the star: '))
draw_star(x,y,length)
