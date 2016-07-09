class Vending_Machine:
    def __init__(self,drink,price):
        self.drink=drink
        self.price=price
    def getDrink(self,coin):
        print(self.drink)
        return_=coin-self.price
        print("Return",return_,"VND")
coin=int(input("Put in your money"))
button=int(input("Enter a number to get a drink(1/2/3)"))
coke=Vending_Machine("Coke",7)
energy=Vending_Machine("Energy",10)
water=Vending_Machine("Water",5)
if button== 1:
    coke.getDrink(coin)
elif button == 2:
    energy.getDrink(coin)
else:
    water.getDrink(coin)

