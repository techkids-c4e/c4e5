#List_assignment2

def sheep(sheep_list):

    print('Now my biggest sheep has size ',max(sheep_list),' lets sheer it')

    res1 = sheep_list.index(max(sheep_list))
    sheep_list[res1] = 8
    print('After sheering, here is my flock ')
    print(sheep_list)
    return sheep_list
   
sheep_list = [12,1,3,20,5,100,17,2]

print('Hello, my name is Huy and these are my ship sizes :')
print(sheep_list)
sheep(sheep_list)
print()
##print('Hello, my name is Huy and these are my ship sizes :')
##print(sheep_list)
##
##print('Now my biggest sheep has size ',max(sheep_list),' lets sheer it')
##
##res1 = sheep_list.index(max(sheep_list))
##sheep_list[res1] = 8
##print('After sheering, here is my flock ')
##print(sheep_list)

for i in range (4) :    
    print('MONTH ',i + 1,' :')
    sheep_list = [50 + sheep_size for sheep_size in sheep_list]
    print('One month has passed, now here is my flock')
    print(sheep_list)
    sheep(sheep_list)
    print()

res = 0
for sheep_size in sheep_list:
    res = res + sheep_size

print("My flock has size in total:",res)
print("I would get",res,"* 5$ =",res * 5)

    
