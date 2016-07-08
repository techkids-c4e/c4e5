class VendingMachine:
    def __init__(self,drink_type,price):
        self.type = drink_type
        self.price = price
    def getdrink(self,coin):
        print("Here is your drink: ",self.type)
        change = coin - self.price
        if change >= 0:
            print("Here is your change: ",change,"VND")
        else:
            print("You need",self.price - coin," VND more for that drink") 

coke = VendingMachine("Coke",7)
energy = VendingMachine("Energy",10)
water = VendingMachine("Water",5)
Type = input("Which drink do you want?(1, 2 or 3): ")
Money = float(input("Give me your money please "))

if Type == "1":
    coke.getdrink(Money)
elif Type == "2":
    energy.getdrink(Money)
elif Type == "3":
    water.getdrink(Money)
else:
    print("Error")
