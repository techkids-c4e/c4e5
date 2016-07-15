class City:
    def __init__(self, name, longt, lat):
        self.name=name
        self.longt=longt
        self.lat=lat

n1=str(input('Please input name of your city: '))
longt1=float(input('Please input longtitude of your city: '))
lat1=float(input('Please input latitude of your city: '))      
c1=City(n1,longt1,lat1)
print('Your city information is: ')
print('Name: ',c1.name)
print('longtitude: ',c1.longt)
print('latitude: ',c1.lat)
