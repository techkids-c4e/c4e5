#tao list size cuu
sizes_list=[5,7,300,90,24,50,75]
print('Hi, i am Ha and these are my sheep sizes')
print(sizes_list)

#tim kich co max
print('Now my biggest sheep has size ',max(sizes_list),' lets shear it')

#sizes sau khi shear

a=max(sizes_list)
sizes_list[sizes_list.index(a)]=8
print('After shearing, , here is my flock')
print(sizes_list)

#tang kich co cuu them 50

new_sizes_list=[50+size for size in sizes_list]
print('One month has passed, now here is my flock')
print(new_sizes_list)

