#rabbits
def fib(n):
    baby,mature = 0,1
    for i in range(n+1):
        baby,mature=mature,baby+mature
    return mature
for i in range(5):
    print("Month ",i,": ",fib(i)," pair(s) of rabbits")

    
