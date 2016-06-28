from turtle import*
def draw_square(d1,d2):
    color(d2)
    for i in range(4):
        forward(d1)
        left(360/4)
l=float(input('Please input length: '))
c=input('Please input color: ')

draw_square(l,c)
        
    
