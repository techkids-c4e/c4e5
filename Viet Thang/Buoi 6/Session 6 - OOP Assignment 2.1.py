class VendingMachine:
    def __init__(self, drinkInfo):
        self.drinkInfo = drinkInfo

    def getDrink(self, coin, button):
        for i in self.drinkInfo:
            if i["buttonx"]==button:
                if coin >= i["cost"]:
                    print("This is your",i["drinkname"],"and",coin - i["cost"],"$")
                else:
                    print("More money, plz")
                
drinkInfo = [
    {'drinkname': 'Coke', 'cost': 7, 'buttonx':1},
    {'drinkname': 'Energy', 'cost': 10, 'buttonx':2},
    {'drinkname': 'Water', 'cost': 5, 'buttonx':3},
        ]  

buy = VendingMachine(drinkInfo)

coin = int(input("Coin: "))
button = int(input("Drink code: 1 for Coke, 2 for Energy and 3 for Water: "))

buy.getDrink(coin, button)
