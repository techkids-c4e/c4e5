##2.1============================================================================
sheep_size = [20, 25, 15, 40, 35]
print("Hello, my name is Hung and these are my sheep's sizes:")
print(sheep_size)
##2.2============================================================================
print("Now my biggest sheep has size", max(sheep_size), ", let's sheer it")
##2.3============================================================================
x = max(sheep_size)
sheep_size[sheep_size.index(x)] = 8
print(sheep_size)
##2.4============================================================================
sheep_size = [size+50 for size in sheep_size]
print('One month has passed, now here is my flock')
print(sheep_size)
##2.5============================================================================
for month 
