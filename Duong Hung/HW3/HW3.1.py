# Import library turtle 


from turtle import *
k=int(input("Number of side: "))
color("green","yellow")
   
begin_fill()
for i in range(k):
    forward(100)
    left(360/k)
end_fill()

