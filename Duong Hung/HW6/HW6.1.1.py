
class City:
    def __init__(self, name, longt, lat):
        self.name=name
        self.longt=longt
        self.lat=lat
    def calculateDistance(self,c):
        x=self.longt - c.longt
        y=self.lat - c.lat
        z=(x**2+y**2)**1/2
        return(z)

n1=str(input('Please input name of first city: '))
longt1=float(input('Please input longtitude of first city: '))
lat1=float(input('Please input latitude of first city: '))      
c1=City(n1,longt1,lat1)

n2=str(input('Please input name of second city: '))
longt2=float(input('Please input longtitude of second city: '))
lat2=float(input('Please input latitude of second city: '))

c2=City(n2,longt2,lat2)

s=c1.calculateDistance(c2)
print('The distance is: ',s)
