class Ninja:
    def __init__(self,name,village,healthPoint,attackPoint,defensePoint):
        self.name = name
        self.village = village
        self.HP = healthPoint
        self.ATK = attackPoint
        self.DEF = defensePoint
    def attack(self, enemy):
        if self.ATK > enemy.DEF:
            enemy.HP = enemy.HP- (self.ATK-enemy.DEF)
        elif self.ATK < enemy.DEF:
            self.HP = self.HP - ( enemy.DEF - self.ATK)
        else:
            enemy.HP = enemy.HP
    def print(self):
        print("Ninja's name:",self.name,"   Village:",self.village,"   HP:",self.HP,"   ATK:",self.ATK,"   DEF:",self.DEF)

Naruto = Ninja("Naruto","Leaf",11,7,4)
Gaara = Ninja("Gaara","Sand",12,6,8)
Zabuza = Ninja("Zabuza","Fog",9,8,3)
Deidara = Ninja("Deidara","Rock",8,10,1)
Ninja_list=[Naruto, Gaara, Zabuza, Deidara]
print("--------------------Naruto attacks Gaara--------------------")
Naruto.attack(Gaara)
for ninja in Ninja_list:
    ninja.print()
print("--------------------Zabuza attacks Naruto--------------------")
Zabuza.attack(Naruto)
for ninja in Ninja_list:
    ninja.print()
print("--------------------Gaara attacks Deidara--------------------")
Gaara.attack(Deidara)
for ninja in Ninja_list:
    ninja.print()
print("--------------------Deidara attacks Zabuza--------------------")
Deidara.attack(Zabuza)
for ninja in Ninja_list:
    ninja.print()
