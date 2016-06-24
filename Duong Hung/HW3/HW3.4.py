# Import library turtle 

from turtle import *
k=int(input("Number of circle: "))
color("green")
speed(0)
for i in range(k):
    circle(100,None,None)
    left(360/k)
