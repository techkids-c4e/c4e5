#1.5 Ask users for their favourite color
color_list=['Blue','Pink','Red','White','Green']
while True:
    mau=input('What is your favourite color?')
    if mau in color_list:
        i=color_list.index(mau)
        print('Your color is at index',i,'in my list')

    else:
        print('Sorry, I could not find your color')
