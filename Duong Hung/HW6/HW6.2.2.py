class Ninja:
    def __init__(self,name,village,HP,ATK,DEF):
        self.name=name
        self.village=village
        self.HP=HP
        self.ATK=ATK
        self.DEF=DEF
    def data(self):
        self.__dict__
    
    def attack(self,enemy):
        if self.ATK >= enemy.DEF:
            a=enemy.HP-(self.ATK-enemy.DEF)
            if a<0:
                enemy.HP=0
            else:
                enemy.HP=a
        return (enemy)

    def one_turn(a,b,c,d):
        a.attack(b)
        c.attack(a)
        b.attack(d)
        d.attack(c)
        print('After one turn:')
        for i in [a,b,c,d]:
          
            print('HP of ',i.name,': ',i.HP)
        
    
    def battle(a,b,c,d):
        while a.HP+b.HP+c.HP+d.HP>max(a.HP,b.HP,c.HP,d.HP):
            a.attack(b)
            c.attack(a)
            b.attack(d)
            d.attack(c)

        for i in [a,b,c,d]:
            if i.HP==max(a.HP,b.HP,c.HP,d.HP):
                print('Winner: ',i.name)

n=input('Please input name of 4 ninja(name1,name2,name3,name4): ')
l=n.split(',')
Nin=[]
j=-1
for i in range(len(l)):
    print('')
    print('Ninja ',l[i])
    t=str(input('Please input information of this ninja(village,HP,ATK,DEF): '))
    k=t.split(',')
    j=j+1
    x=Ninja(l[i],k[0],int(k[1]),int(k[2]),int(k[3]))
    Nin.append(x)

Ninja.one_turn(Nin[0],Nin[1],Nin[2],Nin[3])
print('')
Ninja.battle(Nin[0],Nin[1],Nin[2],Nin[3])
    
