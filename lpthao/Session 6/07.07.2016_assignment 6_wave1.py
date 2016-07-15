class City:
    def __init__(self, name, longt, lat):
        self.name = name
        self.longt = longt
        self.lat = lat
    def calculateDistance(self, another_city):
        x = ((self.longt - another_city.longt)**2 + (self.lat - another_city.lat)**2)**(1/2)
        print("%.2f" % round(x,2))
        
haNoi = City("Hanoi", 50, 75)
haiDuong = City("Haiduong", 25, 10)

haNoi.calculateDistance(haiDuong)





        
