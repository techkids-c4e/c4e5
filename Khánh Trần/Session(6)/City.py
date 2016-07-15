class City:
    def __init__(self,name,longt,lat):
        self.name = name
        self.longt = longt
        self.lat = lat

    def calculateDistance(self,other):
        return ((float(self.longt) - float(other.longt))**2+(float(self.lat) - float(other.lat))**2)**1/2
        
Hanoi = {
 "name" : "Hanoi",
 "longt" : 50,
 "lat" : 75
}
haiduong = {
 "name" : "HaiDuong",
 "longt" : 25,
 "lat" : 10
}


Hanoi = City(Hanoi,50,75)
haiduong = City(haiduong,25,10)

x = Hanoi.calculateDistance(haiduong)

print("The distance is:",x)
