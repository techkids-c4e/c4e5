while True:
    colour_list=['Blue','Red','Black','Pink','Brown','Yellow']
    x=str(input('What is your favourite colour: '))
    j=0
    for i in range(len(colour_list)):
        if colour_list[i]==x:
            print('Your colour is at index ',i,' in my list',)
            j=j+1
    if j==0:
        print('Sorry, I could not find your colour')
    
      
