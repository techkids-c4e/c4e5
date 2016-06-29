#2.1
print('Hello, my name is Minh and these are my ship sizes:')
sheep_list = [5, 7, 300, 90, 24, 50, 75]
print(sheep_list)

#2.2
print('Now my biggest sheep has size of', max(sheep_list), "let's sheer it") 

#2.3
sheep_list.remove(max(sheep_list))
print('After shearing, here is my flock: ')
newflock = sheep_list
print(newflock)

#2.4
newflock2 = [size + 50 for size in newflock]
print(newflock2)

#2.5
for i in range (4) :    
    print('MONTH ',i + 1,' :')
    sheep_list = [50 + sheep_size for sheep_size in sheep_list]
    print('One month has passed, now here is my flock')
    print(sheep_list)
    print()
