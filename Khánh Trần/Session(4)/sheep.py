flock_list = [5,7,300,90,24,50,75]
print("Hello, my name is Khanh and these are my sheep sizes")
print(flock_list)
for x in range(1,4):
    print("Month",x)
    for y in range(6):
        flock_list[y] = flock_list[y] + 50
    print("One month has passed, now here is my flock")
    print(flock_list)
    print("Now my biggest sheep has size",max(flock_list),"let's shear it")
    i = flock_list.index(max(flock_list))
    flock_list.remove(max(flock_list))
    flock_list.insert(i, 8)
    print("After shearig, here is my flock")
    print(flock_list)
    if x == 3:
        sum = 0
        for size in flock_list:
            sum = sum + size
        print("My flock has size in total: ",sum)
        print("I would get", sum,"*2$ =",sum*2,"$")
