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
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300) 
    y = random.randint(-300, 300)
    length = random.randint(3,100)
    draw_star(x,y,length)
# the random.randint(…) statement lets x run randomly from -300 to 300
