while True:
    class VendingMachine:
        def __init__(self,drinkInfo):
            self.drinkInfo=drinkInfo
        def getDrink(self,button,coin):
            for i in self.drinkInfo:
                if i['button']==button:
                    if coin==i['price']:
                        print('here is your ',i['name'])
                    elif coin>i['price']:
                        print('here is your ',i['name'],' and',coin-i['price'])
                    else:
                        print('Please insert more coins')
                        
    drinkInfo=[
        {'name': 'Coke', 'price': 7, 'button':1},
        {'name': 'Energy', 'price': 10, 'button':2},
        {'name': 'Water', 'price': 5, 'button':3}
            ]
    V=VendingMachine(drinkInfo)
    button=int(input('button'))
    coin=int(input('Inser coins'))

    V.getDrink(button,coin)
