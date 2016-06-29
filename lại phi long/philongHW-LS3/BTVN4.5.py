color_list = ['pink', 'red', 'white', 'blue', 'black']
x= input('what is your favorite color? : ')
if x in color_list:
    print('Your color is at index ',color_list.index(x) , 'in my list')
else:
    print('Sorry, I could not find your color.')
    
