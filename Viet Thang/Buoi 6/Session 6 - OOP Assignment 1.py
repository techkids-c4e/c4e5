class city:
    def __init__(self, name, longt, lat):
        self.name = name
        self.longt = longt
        self.lat = lat

    def print(self):
        print("name:",self.name)
        print("longt:",self.longt)
        print("lat:",self.lat)

    def calculateDistance(self, city2):
        x =((self.longt-city2.longt)**2) + (((self.lat-city2.lat)**2)**(1/2))
        print(x)

Hanoi = city("Hanoi",50,75)

#Nhap thong tin 1 thanh pho moi
print("Hello, This is City Distance Caculate System.")
city2 = str(input("Please, Enter your City name: "))
longt2 = float(input("Please, Enter your City’s longitude: "))
lat2 = float(input("Please, Enter your City’s latitude: "))
city2 = city(city2, longt2, lat2)
print("Your City information is: ")
city2.print()

#Tinh khoang cach 2 thanh pho
print("The distance from Hanoi to",city2.name,"is: ")
Hanoi.calculateDistance(city2)




