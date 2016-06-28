from turtle import*
def draw_square(n,a):
    for i in range(n):
        color(a)
        forward(100)
        left(360/n)
##a=str(input("Mau sac: "))
##n=int(input("So canh: "))
for i in range(30):
 draw_square(i * 5, 'red')
 left(17)
 penup()
 forward(i * 2)
 pendown()
