#2.1
list=[5,7,300,90,24,50,75]
print('Hello, my name is Hiep and these are my sheep sizes',list)
#2.2
print('Now my biggest sheep has size', max(list), "let's shear it")
#2.3
list.remove(max(list))
new_list=list
print('Hello, my name is Hiep and here is my flock',new_list)
#2.4
list=[5,7,300,90,24,50,75]
x=list.index(max(list))
list[x]=8
print('After shearing, here is my flock', list)


    
