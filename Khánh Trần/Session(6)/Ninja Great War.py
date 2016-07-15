##l = {
##            "Coke":7,
##            "Energy":10,
##            "Water":5,
##            }
##
##class VendingMachine:
##    def __init__(self,drinkinfo):
##        self.drinkinfo = drinkinfo
##    def  getDrink(self, coin, button):
##        if button == 1:
##            if coin >= 7:
##                print("U will get Coke and",int(coin) - 7,"VND back")
##            else:
##                print("Not enough coins!")
##        elif button == 2:
##            if coin >= 10:
##                print("U will get Energy and",int(coin) - 10,"VND back")
##            else:
##                print("Not enough coins")
##        elif button == 3:
##            if coin >= 5:
##                print("U will get Water and",int(coin) - 5,"VND back")
##            else:
##                print("Not enough coins")
##        else:
##            print("Please choose again")
##
##VendingMachine = VendingMachine(l)
##VendingMachine.getDrink(12,1)
        
class Ninja:
    def __init__(self,name,village,HP,ATK,DEF):
        self.name = name
        self.village = village
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
    def attack(self,enemy):
        HPremaining = self.HP - (enemy.ATK - self.DEF)
        if HPremaining <= 0:
            print(self.name,": KO")
        else:
            print(self.name,"HP remaining:",HPremaining)
            print(enemy.name,"HP remaining:",enemy.HP)

Naruto = Ninja("Naruto","Leaf",11,7,4)
Zabuza = Ninja("Zabuza","Fog",10,8,3)
Gaara = Ninja("Gaara","Sand",12,6,8)
Deidara = Ninja("Deidara","Rock",8,10,1)
while 1:
    
    Naruto.attack(Gaara)
    Zabuza.attack(Naruto) 
    Gaara.attack(Deidara) 
    Deidara.attack(Zabuza)           
        
