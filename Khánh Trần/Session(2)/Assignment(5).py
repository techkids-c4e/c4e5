## a program that calculates the number of pair of rabbit after 4 months
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(8):
    print("Month ",i,": ",fib(i)," pair(s) of rabbits")
