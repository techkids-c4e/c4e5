class City:
    def __init__(self,name,longt,lat):
        self.name=name
        self.longt=longt
        self.lat=lat
    def print(self):
        print("name :", self.name)
        print("longitude :",self.longt)
        print("latitude :",self.lat)
print("Hello, This is City Distance Caculate System")
x = input("Please, Enter your City name: ")
y = input("Please, Enter your City’s longitude: ")
z = input("Please, Enter your City’s latitude: ")
print("Your City information is:")
print("name:", x)
print("longitude:", y)
print("latitude", z)
