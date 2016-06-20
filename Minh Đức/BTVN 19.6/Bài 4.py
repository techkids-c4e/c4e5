B=int(input('Please enter the initial B bacteria number: '))
time=float(input('Thank you! Now, please enter a period of time: '))
if time%2==0:
    print('Total number of B bacteria after this period is: ', time*B)
else:
    Time=time-1
    print('After ',time,'minutes we would have ',Time*B,'bacterias')
