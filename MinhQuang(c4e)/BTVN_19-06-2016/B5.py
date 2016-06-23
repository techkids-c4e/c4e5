baby = 0
mature = 1
for i in range(8):
    print('Month',i,':',mature,'pair(s) of rabbits')
    t = baby
    baby = mature
    mature = mature + t
    
