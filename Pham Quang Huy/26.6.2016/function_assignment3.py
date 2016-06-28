from turtle import*

def draw_star(x ,y , length):
    penup()
    setpos(x, y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)

x = float(input("Enter x coordinate of the star "))
y = float(input("Enter y coordinate of the star "))
l = float(input("Enter length of the star sizes "))
draw_star(x, y, l)
        
