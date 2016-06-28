from turtle import*

def draw_star(x ,y , length):
    penup()
    setpos(x, y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
        

#random.randint(x, y) is a statement will return in a random integer value between x and y, including both ending points
#when we use it, we need to use "random" module by calling (import random)
