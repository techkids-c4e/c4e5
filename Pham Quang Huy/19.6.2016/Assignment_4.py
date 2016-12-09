bacteria_number = int(input('Enter initial B bacteria number : '))
time = float(input('Enter time : '))
t = int(time)
result = bacteria_number * (2 ** (t // 2))
if (result > 1) : 
    print('After ',time,' minutes we would have ',result,' bacterias')
else :
    print('After ',time,' minutes we would have ',result,' bacteria')


