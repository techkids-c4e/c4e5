#2.5
kichco_cuu=[5,7,300,90,24,50,75]
print('Hello, my name is Ha and here is my flock',kichco_cuu)

for month in range(4):  
    if month==0:
        x=max(kichco_cuu)
        print('Now my biggest sheep has size',x,'let us sheer it')
        kichco_cuu[kichco_cuu.index(x)]=8
        print('After sheering, here is my flock',kichco_cuu)
    else:
        print('MONTH',month,':')
        kichco_cuu=[50+size for size in kichco_cuu]
        print('One month has passed, now here is my flock',kichco_cuu)
        if month==3:
            break
        x=max(kichco_cuu)
        print('Now my biggest sheep has size',x,'let us sheer it')
        kichco_cuu[kichco_cuu.index(x)]=8
        print('After sheering, here is my flock',kichco_cuu)
        
#2.6
total_size=sum(kichco_cuu)
print('My flock has size in total:',total_size)
print('I would get',total_size,'* 2$ =',total_size*2,'$')
