a=int(input("Initial B bacteria number: "))
b=int(input("Time(in minutes): "))
k=a
for i in range(2,b+1,2):
    
    k=k * 2
print('After ',b,'minute(s) we would have ',k,'bacterias')

    
