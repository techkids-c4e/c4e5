#rabbits
baby = 0
mature = 1
for i in range(5):
    print("Month ",i,": ",mature + baby," pair(s) of rabbits")
    t = baby
    baby = mature
    mature = mature + t
