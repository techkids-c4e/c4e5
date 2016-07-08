class City:
    def __init__(self,name,longt,lat):
        self.name = name
        self.longitude = longt
        self.latitude = lat
    def print(self):
        print("name: ",self.name)
        print("longitude: ",self.longitude)
        print("latitude: ",self.latitude)

print("Hello, This is City Distance Caculate System.")
n = input("Please, Enter your City name: ")
lo = input("Please, Enter your City’s longitude: ")
la = input("Please, Enter your City’s latitude: ")
print("Your City information is:")
Wave_2 = City(n,lo,la)
Wave_2.print()
