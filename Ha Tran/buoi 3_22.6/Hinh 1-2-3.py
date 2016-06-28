from turtle import*
speed(0)

color('green','yellow')
begin_fill()
#square
for i in range(4):
    forward(100)
    left(90)
penup()
backward(200)
pendown()
#right triangle
for i in range(3):
    forward(100)
    left(120)
penup()
backward(200)
pendown()
#circle
for i in range(360):
    forward(1)
    left(1)
end_fill()


