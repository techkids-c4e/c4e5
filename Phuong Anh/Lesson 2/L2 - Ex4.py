print('Exercise 4: To calculate number of bacteria')
while True:
    x = int(input('Number of initial bacteria: ')) # so vi khuan ban dau
    minute = float(input('Time in minutes: ')) # thoi gian
    bacteria = x*2**(int(minute//2))
    print(str.format('After {0} minutes, there are {1} bacteria.',minute,bacteria))

