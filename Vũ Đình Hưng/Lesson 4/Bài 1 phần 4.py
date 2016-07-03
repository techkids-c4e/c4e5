##1.1============================================================================
color_list = ['Purple', 'Black', 'Red', 'Blue', 'Green', 'White']
##1.2============================================================================
print('color_list at index 3:', color_list[3])
##1.3============================================================================
x = int(input ('Enter a number from 0-5: '))
print('color_list at index', x, color_list[x])
##1.4============================================================================
print(color_list)
for my_color in color_list:
    print(my_color)
##1.5============================================================================
user_color = str(input('What is your favorite color'))
if user_color in color_list:
    print('your color is at index', color_list.index(user_color), 'in my list')
