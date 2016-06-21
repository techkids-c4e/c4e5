print('Exercise 4: To calculate number of bacteria')
x = int(input('Number of initial bacteria: '))
minute = float(input('Time in minutes: '))
if minute%2==0 or int(minute)%2==0:
    bacteria = int(x*2**(int(minute)/2))
else:
    bacteria = int(x*2**(int(minute-1)/2))
print(str.format('After {0} minutes, there are {1} bacteria.',minute,bacteria))

