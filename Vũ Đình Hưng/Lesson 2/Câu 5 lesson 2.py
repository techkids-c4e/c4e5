count = 0
x = 4
y = 6
for a in range (4):
    old_x = x
    old_y = y
    x = old_y
    y = old_x + old_y
    print (old_x)
