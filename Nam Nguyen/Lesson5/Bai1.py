from turtle import*
def draw_square(n,a):
    for i in range(n):
        color(a)
        forward(100)
        left(360/n)
n=int(input("So canh: "))
a=str(input("Mau sac: "))
draw_square(n,a)

