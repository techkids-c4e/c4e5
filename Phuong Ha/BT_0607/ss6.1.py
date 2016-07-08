## wave 1

class City:
    def __init__(self,name,longt,lat):
        self.name=name
        self.longt=longt
        self.lat=lat
    def calculateDistance(self,city2):
        distance=((self.longt-city2.longt)**2) + (((self.lat-city2.lat)**2)**(1/2))
Hanoi=City("Hanoi",50,75)
Haiduong=City("Haiduong",25,10)
x=Hanoi.calculateDistance(Haiduong)
print(x)

##wave2

name=input('Ten thanh pho: ')
longt=input('vi do: ')
lat=input('kinh do: ')
class Cities:
    def __init__(self,name,longt,lat):
        self.name=name
        self.longt=longt
        self.lat=lat
    def print(self):
        print('thanh pho: ',self.name)
        print('vi do: ',self.longt)
        print('kinh do: ',self.lat)
c=Cities(name,longt,lat)
c.print()
