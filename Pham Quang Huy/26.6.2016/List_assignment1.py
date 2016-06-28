color_list = ['Blue','Red','Black','Pink','Brown','Yellow']
print('My color list: ')
print(color_list)
print('Color_list at index 3: ',color_list[3])
i = input('Enter a number for 0-5: ')
i = int(i)
print('Your color: ',color_list[i])
print(color_list)
for color in color_list:
    print(color)
fav_color = input('Whats your favourite color: ')
color_list.append(fav_color)
t = color_list.index(fav_color)
if t == 6 :
    print('Sorry, I could not find your color')
else :
    print('Your color is at index ',t,' in my list')
    
