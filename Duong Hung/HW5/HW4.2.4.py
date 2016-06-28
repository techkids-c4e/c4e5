a=str(input('What is your name: '))
x=input('Please input list of your flock size: ')
x=eval(x)
print('')
print('Hello, my name is ',a,' and there are my ship sizes: ')
print(x)
print('')
print('Now my biggest sheep has size ',max(x)," let's shear it")
print('')
m=x.index(max(x))
x[m]=8
print('After shearing, here is my flock ')
print(x)
print('')
for i in range(len(x)):
    x[i]=x[i]+50
print('One month has passed, now here is my flock')
print(x)
