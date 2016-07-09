class City:
    def __init__(self,longt,lat):
        self.longt = longt
        self.lat = lat
    def calculateDistance(self, city):
        distance =  ((self.longt-city.longt)**2+(self.lat-city.lat)**2)**(1/2)

        return(distance)
Hanoi = City(50,75)
Haiduong = City(25,10)
x= Hanoi.calculateDistance(Haiduong)
print(x)
