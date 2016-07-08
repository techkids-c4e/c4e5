class City:
    def __init__(self,name,longt,lat):
        self.name=name
        self.longt=longt
        self.lat=lat
    def print(self):
        print("name :", self.name)
        print("longitude :",self.longt)
        print("latitude :",self.lat)

x=input("Hello, This is City Distance Caculate System")
y=input("Please, Enter your City name")
z=input('Please, Enter your City’s longitude')
i=input('Please, Enter your City’s longitude')
c=City(y,z,i)
c.print()
