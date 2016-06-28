a=str(input('What is your name: '))
x=input('Please input list of your flock size: ')
m=int(input('Please input number of months: '))
x=eval(x)
print('')
print('Hello, my name is ',a,' and there are my ship sizes: ')
print(x)
print('')
def flock(y):
    for i in range(len(y)):
        y[i]=y[i]+50
    print('One month has passed, now here is my flock')
    print(x)
    print('Now my biggest sheep has size ',max(y)," let's shear it")
    m=y.index(max(y))
    y[m]=8
    print('After shearing, here is my flock ')
    print(x)
    print('')

for j in range(m):
      print('MONTH ',j+1)
      flock(x)


    
    
