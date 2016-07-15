drink_type = ["Shit, ""Coke", "Energy", "Water"]
list_ = [0,{
    "name" : "Coke",
    "cost" : 7
    },{
    "name" : "Energy",
    "cost" : 10
    },{
    "name" : "Water",    
    "cost" : 5 
    }]
def Input_():
    str = (input("Pls put coin and press on drink: ").split(" "))
    str[0] = int(str[0])
    str[1] = int(str[1])
    return(str)
    
class VendingMachine:
    def __init__(obj,drinkInfo):
        obj.drinkInfo = drinkInfo
    def getDrink(obj, coin, button):
        cost = obj.drinkInfo[button]["cost"]
        if cost > coin :
            print("Please try again, you cant afford this product")
        else :
            return_ = coin - cost
            print("Here's your", obj.drinkInfo[button]["name"])
            print("Here's your return money", return_)

maynuoc = VendingMachine(list_)
while True:
    a = Input_();
    ##print(a[0])
    ##print(a[1])
    maynuoc.getDrink(a[0],a[1])
    
    
        
        
        
        
