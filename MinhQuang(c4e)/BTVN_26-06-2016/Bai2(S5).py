from turtle import*
def draw_square(d,y):
    color(y)
    for i in range(4):
        fd(d)
        left(360/4)
y = str(input('Enter the color: '))
d = int(input('Enter the length: '))
        
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
