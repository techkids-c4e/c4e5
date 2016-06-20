bacteria_number = int(input('Enter initial B bacteria number : '))
time = int(input('Enter minutes : '))
result = bacteria_number* (2**(time // 2))
if (result > 1) : 
    print('After ',time,' minutes we would have ',result,' bacterias')
else :
    print('After ',time,' minutes we would have ',result,' bacteria')
