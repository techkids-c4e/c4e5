from turtle import*
def draw_star(x,y,length):
    penup()
    setpos(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
x=float(input("enter x  "))
y=float(input("enter y  "))
l=float(input("Enter length of size"))
draw_start(x,y,l)
