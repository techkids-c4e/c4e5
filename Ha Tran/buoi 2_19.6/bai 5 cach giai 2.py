def fib(n):                     # write Fibonacci series up to n
    if n<1:                     #thang 0 thi f(0) bang 1
        return 1
    return fib(n-1)+fib(n-2)    #Cac thang con lai: so cap tho thang n bang tong so cap tho thang (n-1) va thang (n-2)
for month in range(5):          #Trong 4 thang dau tien
    print('Month ',month,' :',fib(month),' pair(s) of rabbits')#Hien thi ket qua
    
