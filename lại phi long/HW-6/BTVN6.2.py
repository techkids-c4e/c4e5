class Ninja:
    def __init__(self, name, village, healthPoint, attackPoint, defensePoint):
        self.ninjaname = name
        self.village = village
        self.healthPoint = healthPoint
        self.attackPoint = attackPoint
        self.defensePoint = defensePoint
    def attack(self, name2):
        damage = self.attackPoint - name2.defensePoint
        if damage <= 0:
            self.healthPoint = self.healthPoint + damage
            print(self.ninjaname, "healthPoint is: ", self.healthPoint)
        elif damage > 0:
            name2.healthPoint = name2.healthPoint - damage 
            print(name2.ninjaname, "healthPoint is: ", name2.healthPoint)
Naruto = Ninja("Naruto", "leaf village", 11, 7, 4)
Gaara = Ninja("Gaara", "sand village", 12, 6, 8)
Zabuza = Ninja("Zabuza", "fog village", 9, 8, 3)
Deidara = Ninja("Deidara", "rock village", 8, 10, 1)
for attack_number in range (2):
    Naruto.attack(Gaara)
    Zabuza.attack(Naruto)
    Gaara.attack(Deidara)
    Deidara.attack(Zabuza)
    print(Gaara.ninjaname, "healthPoint is: ",Gaara.healthPoint)
max_health = Naruto.healthPoint
if max_health < Deidara.healthPoint:
    max_health== Deidara.healthPoint
elif max_health < Zabuza.healthPoint:
    max_health== Zabuza.healthPoint
elif max_health < Gaara.healthPoint:
    max_health== Gaara.healthPoint
print(max_health.ninjaname)

