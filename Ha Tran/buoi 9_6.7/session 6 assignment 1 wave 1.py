#wave 1
hanoi = {"name" : "Hanoi",
         "longt" : 50,
         "lat" : 75}

haiduong = {"name" : "HaiDuong",
            "longt" : 25,
            "lat" : 10}
cities=[hanoi,haiduong]
class City:
    def __init__(self,city1):
        self.n=city1["name"]
        self.lo=city1["longt"]
        self.la=city1["lat"]

    def calculateDistance(self,city2):
        distance=(((city2["longt"]-self.lo)**2+(city2["lat"]-self.la)**2)**0.5)
        distance=round(distance,2)
        return distance


Hanoi=City(hanoi)
x=Hanoi.calculateDistance(haiduong)
print('The distance is: ',x)


