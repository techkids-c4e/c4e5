big_rabbit=1
little_rabbit=0
thang=int(input('Please enter month: '))
for Thang in range(thang+1):
    print('Month',Thang,':' , big_rabbit,'pair(s) of rabbits')
    x=little_rabbit
    little_rabbit=big_rabbit
    big_rabbit=x+big_rabbit
        
        
        
