Coke={"drinktype":"Coke",
      "price":7
      }
Energy={"drinktype":"Energy",
        "price":10
        }

Water={"drinktype":"Water",
        "price":5
        }
drinkdict=[Coke,Energy,Water]

#Cach 1:
class VendingMachine:
    
    def __init__(self,drinkInfo):
        self.drinkdict=drinkdict
    def getDrink(self,coin,button):
        chosen_drink=self.drinkdict[button-1]["drinktype"]
        print('The chosen drink:',chosen_drink)
        excessive=coin-self.drinkdict[button-1]["price"]
        print("excessive charge:",excessive)
    

drink=VendingMachine(drinkdict)
c=int(input('Put coin').strip())
b=int(input('Press 1 2 or 3').strip())
drink.getDrink(c,b)


#Cach 2:
class VendingMachine:  
    def __init__(self,drink):
        for drink in drinkdict:
            self.drink=drink
    def getDrink(self,coin,button):
        if button==1:
            self.drink=Coke
        elif button==2:
            self.drink=Energy
        elif button==3:
            self.drink=Water
        change=coin-self.drink["price"]
        print('The chosen drink',self.drink["drinktype"])
        print("excessive charge:",change)

Coke=VendingMachine(Coke)
c=int(input('Put coin').strip())
b=int(input('Press 1 2 or 3').strip())
Coke.getDrink(c,b)
