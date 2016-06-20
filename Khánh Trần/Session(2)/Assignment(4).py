##a program that calculate and print out the total number of B bacteria after a period of time
b1 = int(input('Pls enter the initial B bacteria number: '))
t = float(input(' & the time is: '))
if t > 1 :
    b2 = int(b1*(t//2))
    print('After',t,'minues we would have',b2,'bacterias')
else:
    print('After',t,'minues we would have',b1,'bacterias')
