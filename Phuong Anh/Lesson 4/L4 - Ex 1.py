#1.1
print('Question 1.1')
colour_list = ['blue', 'red', 'green', 'orange', 'pink', 'purple']
print(colour_list)

#1.2
print('Question 1.2')
print(colour_list[3]) #to print colour at position 3

#1.3
print('Question 1.3')
i = int(input('Enter a number from 0 to 5: '))
print('Your colour: ', colour_list[i])

#1.4
print('Question 1.4')
print(colour_list)
for i in colour_list:
    print(i)

#1.5
print('Question 1.5')
i = input('What is your favourite colour? ')
if i in colour_list:
    print('Your colour is at index', colour_list.index(i),'in my list')
else:
    print('Sorry I could not find your colour')
