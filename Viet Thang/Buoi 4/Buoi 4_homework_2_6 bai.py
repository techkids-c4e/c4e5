# Session 4 - 2.1
size_list=[5,7,300,90,24,50,75]
print('Hello, my name is Thang and these are my sheep sizes:')
print(size_list)

# Session 4 - 2.2

length=len(size_list)
biggest_sheep=size_list[0]
for i in range(length):
    if biggest_sheep < int(size_list[i]):
        biggest_sheep=size_list[i]

print('Now my biggest sheep has size',biggest_sheep,'lets shear it')

# Session 4 - 2.3
for i in range(length):
    if int(size_list[i])==int(biggest_sheep):
        size_list[i]=8
print('After shearing, here is my flock')
print(size_list)

# Session 4 - 2.4
size_list_1month = [50 + sheep for sheep in size_list]
print('One month has passed, now here is my flock:')
print(size_list_1month)

# Session 4 - 2.5
thang=int(input('Ban muon biet kich thuoc cuu sau may thang? '))
for n in range(thang):

    
    
    size_list = [50 + sheep for sheep in size_list]
    length= len(size_list)

    print('MONTH',n+1)
    print('One month has passed, now here is my flock:')
    print(size_list)

    biggest_sheep=size_list[0]
    for i in range(length):
        if biggest_sheep < int(size_list[i]):
            biggest_sheep=size_list[i]

    print('Now my biggest sheep has size',biggest_sheep,'lets shear it')

    for i in range(length):
        if int(size_list[i])==int(biggest_sheep):
            size_list[i]=8
    
    print('After shearing, here is my flock')
    print(size_list)

# Session 4 - 2.6
Total_size=0
for i in range(length):
    Total_size=Total_size + size_list[i]
print('My flock has size in total: ',Total_size)
print('I would get',Total_size,'* 2$ = ',Total_size*2,'$')
