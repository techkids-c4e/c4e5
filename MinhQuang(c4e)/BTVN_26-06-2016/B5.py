while True:
    favorite_color = ['Blue', 'Red', 'Black', 'Pink', 'Brown', 'Yellow']
    x = str(input('What is your favorite color? '))
    for name in range(len(favorite_color)):
        if favorite_color[name] == x:
            print('Your color is at index ',i,' in my list')
        else:
            print('Sorry, I could not find your color')
