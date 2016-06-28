#viet ham ve hinh n canh voi 2 tham so dau vao: d: do dai canh, n: so canh
from turtle import*
while True:
    d=int(input('nhap do dai'))
    n=int(input('nhap so canh'))
    def ve_hinh(d,n):
        for i in range(n):
            forward(d)
            left(360/n)
        return d
        return n
    ve_hinh(d,n)
