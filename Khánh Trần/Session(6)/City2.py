class City:
    def __init__(self,name,longt,lat):
        self.name = name
        self.longt = longt
        self.lat = lat
    def Ask(self):
       print("Your City information is: ")
       print("name:",self.name)
       print("longtitude:",self.longt)
       print("latitude:",self.lat)
print("Hello, This is City Distance Caculate System")
x = input("Please, Enter your City name: ")
y = int(input("Please, Enter your City’s longitude: "))
z = int(input("Please, Enter your City’s latitude: "))
City = City(x,y,z)
City.Ask()
