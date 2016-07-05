#2.1
kichco_cuu=[5,7,300,90,24,50,75]
print(type(size for size in kichco_cuu))
print('Hello, my name is Ha and these are my sheep sizes',kichco_cuu)
#2.2: search for the biggest sheep in the list
x=max(kichco_cuu)
print('Now my biggest sheep has size',x,'let us sheer it')
#2.3 Print your sheep size after sheering the biggest one
kichco_cuu[kichco_cuu.index(x)]=8
print('After sheering, here is my flock',kichco_cuu)
#2.4 increased by 50
##for i in range(6):
##    kichco_cuu[i]=kichco_cuu[i]+50
##print('One month has passed, now here is my flock',kichco_cuu)
new_list=[50+size for size in kichco_cuu]
print('One month has passed, now here is my flock',new_list)
