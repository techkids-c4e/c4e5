a=1
b=1
x=int(input("Input number of month: "))
for i in range(x):
    b=a+b
    a=b-a

print('Month ', x,': ',b,' pair(s) of rabbits')
