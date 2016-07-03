from turtle import *
def draw_star(x, y, length):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range (5):
        forward(length)
        left(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
##công du.ng cu?a random.randint là ta.o ra mô.t sô' x bâ't kì sao cho x thoa?
##mãn x là sô' nguyên và x thuô.c khoa?ng tu\ a dê'n b.
