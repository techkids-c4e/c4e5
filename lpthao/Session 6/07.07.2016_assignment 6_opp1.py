class VendingMachine:
    def __init__(self):
        self.coin = 0
        self.button = 0
        self.drinkType = [
            {
                "name" : "Coke", "price" : 7 , "button" : 1
            },
            {   "name" : "Energy", "price" : 10 , "button" : 2
            },
            {
                "name" : "Water", "price" : 5 , "button" : 3
            }
            
        ]
    def getDrink(self): 
        self.coin = int(input("coin:"))
        self.button = int(input("button:"))
    def print(self):
        for i in self.drinkType:
            if i["button"] == self.button:
                print("Drink Type:", i["name"])
                print("Excessive change:", self.coin - i["price"])

p = VendingMachine()
p.getDrink()
p.print()

