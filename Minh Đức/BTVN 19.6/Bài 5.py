big_rabbit=1
little_rabbit=0
for thang in range(4):
    print('Month',thang,':' , big_rabbit,'pair(s) of rabbits')
    x=little_rabbit
    little_rabbit=big_rabbit
    big_rabbit=x+big_rabbit
        
        
        
