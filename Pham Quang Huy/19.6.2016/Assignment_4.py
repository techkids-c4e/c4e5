bacteria_number = int(input('Enter initial B bacteria number : '))
time = int(input('Enter time : '))
result = 2 ** (time // 2)
if (result > 1) : 
    print('After ',time,' minutes we would have ',result,' bacterias')
else :
    print('After ',time,' minutes we would have ',result,' bacteria')


