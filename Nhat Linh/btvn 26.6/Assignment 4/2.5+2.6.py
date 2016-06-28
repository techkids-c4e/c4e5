list = [5,7,300,90,24,50,75]
print("Hello, my name is Hiep and here is my flock",list)
print("Now my biggest sheep has size",max(list),"let's shear it")
a = list.index(max(list))
list[a]=8
print("After shearing, here is my flock")
print(list)

for month in range(1,4):
    print("Month",month)
    for y in range(7):
        list[y] = list[y] + 50
    print("One month has passed, now here is my flock")
    print(list)
    print("Now my biggest sheep has size",max(list),"let's shear it")
    a = list.index(max(list))
    list[a]=8
    print("After shearing, here is my flock")
    print(list)
    
a=sum(list)
print('My flock has size in totoal:',a)
print('I would get',a, '*2$ = ',a*2,"$")

