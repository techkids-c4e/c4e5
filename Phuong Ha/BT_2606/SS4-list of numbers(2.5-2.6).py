##qua trinh 4 thang
sizes_list=[5,7,300,90,24,50,75]
print('Hi, i am Ha and these are my sheep sizes')
print(sizes_list)

print('Month 1:')
new_sizes_list=[50+size for size in sizes_list]
print('One month has passed, now here is my flock')
print(new_sizes_list)

def sheep():
    print('Now my biggest sheep has size ',max(new_sizes_list),' lets shear it')
    a=max(new_sizes_list)
    new_sizes_list[new_sizes_list.index(a)]=8
    print('After shearing, , here is my flock')
    print(new_sizes_list)
    return new_sizes_list
sheep()
for i in range (2,4):
    print('Month ',i,' :')
    new_sizes_list=[50+ size for size in new_sizes_list]
    print('One month has passed, now here is my flock')
    print(new_sizes_list)
    sheep()

##ban cuu
a=sum(new_sizes_list)
print('My flock has size in total: ',a)
money= a*2
print('I would get ',a,' *2$ = ',money,'$')
