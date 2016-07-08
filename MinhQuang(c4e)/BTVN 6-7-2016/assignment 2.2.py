class Ninja_school:
    def __init__(self,name,village,HP,ATK,DEF):
        self.ninjaname = name
        self.village=village
        self.HP=HP
        self.ATK=ATK
        self.DEF=DEF
    def attack(self,name):
        damage = self.ATK - name.DEF
        name.HP = name.HP - damage
        print(name.ninjaname, "HP is: ",name.HP)

Naruto=Ninja_school("Naruto", "leaf village", 11, 7, 4)
Gaara=Ninja_school("Gaara","sand village", 12,6 ,8)
Zabuza=Ninja_school("Zabuza","fog village", 9, 8, 3)
Deidara=Ninja_school("Deidara","rock village", 8, 10, 1)
for attack_number in range(2):
    Naruto.attack(Gaara)
    Zabuza.attack(Naruto)
    Gaara.attack(Deidara)
    Deidara.attack(Zabuza)
    print(Gaara.ninjaname, "HP is", Gaara.HP)


