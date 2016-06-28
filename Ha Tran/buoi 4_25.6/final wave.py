u='bighero6'
p='codethechange'
while True:
    n=input('enter your user name:')
    if n=='':
            print('you must enter your username')
    elif n!=u:
        print('username is invalid')
    elif n==u:
        while True:
            m=input('enter your password')
            if m==p:
                print('welcome to techkids 2016')
            else:
                print('incorrect password')
        if m ==p:
            break
            
        
    


