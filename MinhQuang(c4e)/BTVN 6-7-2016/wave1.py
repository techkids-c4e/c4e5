hanoi = {"name":"Hanoi",
         "longt":50,
         "lat": 75}
haiduong = {"name" : "HaiDuong",
            "longt" : 25,
            "lat":10}
class City:
    def __init__(self,name,longt,lat):
        self.name = name
        self.longt = longt
        self.lat = lat
    def calculateDistance(self, other):
        distance = ((self.longt-other.longt)**2 + (self.lat-other.lat)**2) **(1/2)
        return distance
Hanoi = City("Hanoi",50,75)
HaiDuong = City("HaiDuong",25,10)
x = Hanoi.calculateDistance(HaiDuong)
print("The distance is:",x)
