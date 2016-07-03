#Session 4 - 1.1

color_list = ['Blue','Red','Black','Pink', 'Brown', 'Yellow']
print('My color list')
print(color_list)

# Session 4 - 1.2

print('color_list at index 3: ',color_list[3])
    
# Session 4 - 1.3

i = int(input('enter a number from 0-5:'))
print('Your color: ',color_list[i])

# Session 4 - 1.4
print(color_list)
for color in color_list:
    print(color)

# Session 4 - 1.5
mausac = str(input('What is  your favorite color? '))
length = len(color_list)
for i in range(length):
    if color_list[i]==str(mausac):
        print('Your color is at index',i,'in my list')
    else:
        print('Sorry, i could not find your color')
    
