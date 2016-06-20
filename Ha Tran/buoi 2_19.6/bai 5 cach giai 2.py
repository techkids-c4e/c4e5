def fib(n):# write Fibonacci series up to n
    if n<2:
        return n+1
    return fib(n-1)+fib(n-2)
for month in range(5):
    print('Month ',month,' :',fib(month),' pair(s) of rabbits')
    
