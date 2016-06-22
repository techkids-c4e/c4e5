print('Exercise 5: Number of pair of rabbit after 4 month')
for month in range(15):
    def rabbit(month):
        if month == 0:
            return 1
        elif month == 1:
            return 2
        else:
            return rabbit(month-1) + rabbit (month-2)
    print(str.format('Month {0}: {1} pair(s) of rabbits',month,rabbit(month)))
