##while True:
##    n=int(input('enter a number:'))
##    if n%2==0:
##        print('this is a even number')
##    else:
##        print('this is a odd number')
    
while True:
    n=int(input('enter a number:'))
    if n%2==0:
        print('this is a even number')
        if int(n**0.5)**2==n:
            print('day la so chinh phuong')
        elif n<0:
            print('khong phai so chinh phuong')
        else:
            print('khong phai so chinh phuong')
    else:
        print('this is a odd number')
