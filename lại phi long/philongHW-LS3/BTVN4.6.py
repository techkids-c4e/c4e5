size_list = [5, 3, 8903, 895, 62, 71, 90, 2016]
print (' Hi, my name is Long and these are my sheep sizes: ', size_list)
for i in range (4):
    for x in range (8):
        size_list[x] = size_list[x] + 50
    print ('One month has passed, now here is my flock: ', size_list)
    print (' Now my biggest sheep has size ',max(size_list)," let's shear it ")
    size_list[size_list.index(max(size_list))] = 8
    print ('After shearing, here is my flock', size_list)
x=0
for _ in range (8):
    x= x+ size_list[_]
print('My flock has size in total: ', x)
print ('I would get ',x ,'*2$ = ',x*2 ,'$' )
    

