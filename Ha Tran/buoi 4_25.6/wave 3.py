from turtle import*
while True:
    n=input('Choose direction:')
    if n=='right':
        right(60)
        forward(100)
    elif n=='left':
        left(60)
        forward(100)
    else:
        print('go lai')
    
