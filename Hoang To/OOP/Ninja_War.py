# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:00:29 2016

@author: Hoang.To
"""

class Ninja:
    def __init__(self,HP,ATK,DEF):
        self.HP=HP
        self.ATK=ATK
        self.DEF=DEF
    def attack(self,enemy):
#        if self.HP>0:        
        enemy.HP=enemy.HP-(self.ATK-enemy.DEF)
        
Naruto=Ninja(11,7,4)
Gaara=Ninja(12,6,8)
Zabuza=Ninja(9,8,3)
Deidara=Ninja(8,10,1)


list=[Naruto,Zabuza,Gaara,Deidara]

while len(list)>1:
    list=[ i for i in  [Naruto,Zabuza,Gaara,Deidara] if i.HP>0]
    Naruto.attack(Gaara)
    print(str(Naruto.HP))
    Zabuza.attack(Naruto)
    print(str(Zabuza.HP))
    Gaara.attack(Deidara)
    print(str(Zabuza.HP))
    Deidara.attack(Zabuza)
    print(str(Deidara.HP))
#print (str(list[0].HP))