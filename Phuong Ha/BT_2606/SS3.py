## ve h.vuong theo do dai, mau
from turtle import*
def draw_square(l,c):
    color(c)
    for x in range(4):
        fd(l)
        left(90)
l=int(input('Length : '))
c=input('color : ')
draw_square(l,c)

#them 1 doan code
for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    fd(i*2)
    pendown()

##ve sao
def draw_star(x,y,l):
    penup()
    setx(x)
    sety(y)
    pendown()
    for x in range (5):
        fd(l)
        right(144)
   
draw_star(50,50,100)

#them 1 doan code
speed(0)
color('blue')
for i in range(100):
    import random
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    l=random.randint(3,10)
    draw_star(x,y,l)
    
# random.randint la cau lenh chon so ngau nhien trong mot khoang(tinh ca 2 dau mut)
#cach dung : chon x ngau nhien trong khoang a den b:  x=random.randint(a,b)


##bo $ trong str
def remove_dollar_sign(s):
    return(s.replace('$',''))

#test code

string_with_no_dollars = remove_dollar_sign("$80% perce$nt of l$ife is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
     print('Your function is correct')
else:
     print('Oops. there is a bug')
     
##extract even items
def extract_even(l):
    x=[]
    for i in l:
        if i%2 == 0:
            x.append(i) 
    return x
l=[1,2,3,4]
print(extract_even(l))

# test code
even_list=extract_even([1,2,5,-10,9,6])
if set(even_list)==set([2,-10,6]):
    print('your function is correct')
else:
    print('oops, bugs detected')
