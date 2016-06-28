from turtle import*
x=int(input('location 1'))
y=int(input('location 2'))
length=int(input('length'))
def draw_star(x,y,length):
    penup()
    setposition(x,y)
    pendown()
    for x in range(5):
        forward(length)
        right(144)
draw_star(x,y,length)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
draw_star(x, y, length)

#random.randint(a, b):Return a random integer N such that a <= N <= b.
#how to use it: import the random module and use random functions needed.
