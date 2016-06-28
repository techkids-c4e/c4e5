#2.1
print('Question 2.1')
print('Hello, my name is Phuong Anh and these are my ship sizes:')
ship_size = [5, 7, 300, 90, 24, 50, 75]
print(ship_size)

#2.2
print('Question 2.2')
print('Now my biggest sheep has size of', max(ship_size), "let's sheer it") #max la gia tri lon nhat trong list

#2.3
print('Question 2.3')
ship_size.remove(max(ship_size))
print('After shearing, here is my flock: ')
new_flock_1 = ship_size
print(new_flock_1)

#2.4
print('Question 2.4')
new_flock_2 = [size + 50 for size in new_flock_1]
print(new_flock_2)




