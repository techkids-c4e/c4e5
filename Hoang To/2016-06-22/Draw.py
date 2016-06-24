from turtle import *

x=int(input("Hay nhap so canh cua hinh muon ve: "))
color("red","blue")
speed(1)
for y in range(x):
    forward(100)
    left(360/x)
fillcolor("yellow")
