
class drink:
        def __init__(self,name,price,button):
            self.name=name
            self.price=price
            self.button=button

drinkInfo={drink('Coke',7,1),
            drink('Energy',10,2),
            drink('Water',5,3)}


class VendingMachine:
    def __init__(self,name):
        self.name=name
    
    
    
    def getDrink(self,coin,button):

        for d in drinkInfo:
            
            if d.button==button:
                if coin < d.price:
                    print('Your coin is lower than price of drink, please re-input')
                else:
                    print('Drink type: ',d.name)
                    print('The excessive change: ',d.price)

n=str(input('Please input name of Machine: '))
m=VendingMachine(n)
while True:
    c=float(input('Please input your coin: '))
    b=int(input('Please input your button: '))
    m.getDrink(c,b)
    
