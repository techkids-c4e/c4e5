from turtle import*
def draw_star(x,y,length):
    penup()
    setpos(x,y)#set initial position
    pendown()
    for i in range(5):
        forward(length)
        right(144)
            
speed(0)
color("blue")
for i in range(100):
    import random #to import "random"
    x = random.randint(-300, 300) #return a random integer N such that -300<= N <=300
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x,y,length)




