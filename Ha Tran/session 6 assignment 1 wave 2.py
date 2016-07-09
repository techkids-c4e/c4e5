#wave 2
class City:
    def __init__(self,name,longt,lat):
        self.n=name
        self.lo=longt
        self.la=lat

    def print(self):
        print('Your City information is:\nname:',self.n,'\nlongitude:',self.lo,'\nlatitude:',self.la)
  
print('Hello, This is City Distance Caculate System.')
name=input('Please, Enter your City name: ')
longt=input('Please, Enter your City’s longitude: ')
lat=input('Please, Enter your City’s latitude: ')


NewCity=City(name,longt,lat)
NewCity.print()
            
