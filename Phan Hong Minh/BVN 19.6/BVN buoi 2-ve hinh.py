from turtle import *

for side in range (7,2,-1):
    if side%2 == 0:
        color("blue", "green")
    else:
        color("red", "yellow")
    begin_fill()
    for i in range(side):
       forward(100)
       left(360/side)
    end_fill()



