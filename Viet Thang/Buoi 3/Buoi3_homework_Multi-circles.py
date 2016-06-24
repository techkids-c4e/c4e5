
#Multi-circles
from turtle import *

color("green")

sovongtron = int(input("Ban muon ve bao nhieu vong tron? "))

for n in range(sovongtron):
    for side in range(360):
        forward(1)
        left(1)
        speed(0)
    left(360/sovongtron)
    
