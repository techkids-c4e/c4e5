class Ninja:
    def __init__(self,name,village,healthPoint, attackPoint, defensePoint):
        self.name = name
        self.village = village
        self.healthPoint = healthPoint
        self.attackPoint = attackPoint
        self.defensePoint = defensePoint

    def attack(self, enemy):
        if self.healthPoint > 0 :
            enemy.healthPoint = max(0,enemy.healthPoint - max(0,(self.attackPoint - enemy.defensePoint)))

##    def Print(self):
##        return(self.healthPoint)

Naruto  = Ninja("Naruto", "Leaf", 11 , 7, 4)
Gaara   = Ninja("Gaara", "Sand", 12, 6, 8)
Zabuza  = Ninja("Zabuza", "Fog", 9, 8, 3)
Deidara = Ninja("Rock", "Rock", 8, 10, 1)

a = [0, 0 , 0, 0]
b = ["Naruto", "Gaara", "Zabuza", "Deidara"]
Naruto.attack(Gaara)
Zabuza.attack(Naruto)
Gaara.attack(Deidara)
Deidara.attack(Zabuza)

def check():
    print("As the battle went on, ninja standing at last are:")
    for i in range(4):
        if a[i] > 0:
            print(b[i])  

while True:
    a[0] = Naruto.healthPoint
    a[1] = Gaara.healthPoint
    a[2] = Zabuza.healthPoint
    a[3] = Deidara.healthPoint
    Naruto.attack(Gaara)
    Zabuza.attack(Naruto)
    Gaara.attack(Deidara)
    Deidara.attack(Zabuza)

    if a[0] == Naruto.healthPoint and a[1] == Gaara.healthPoint and a[2] == Zabuza.healthPoint and a[3] == Deidara.healthPoint :
        check();
        break;

