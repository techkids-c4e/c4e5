class City:
    def __init__(self, name, longt, lat):
        self.name=name
        self.longt=longt
        self.lat=lat
   

#wave1    
##    def calculateDistance(self, another_city):
##        x = ((self.longt - another_city.longt)**2 + (self.lat - another_city.lat)**2)**(1/2)
##        print("khoang cach hai thanh pho", self.name, another_city.name, "la:")
##        print(x)
##        
##haNoi = City("Hanoi", 50, 75)
##haiDuong = City("Haiduong", 25, 10)
##
##
##haNoi.calculateDistance(haiDuong)

#wave2
    def info(self):
        print("name:",self.name)
        print("longitude:",self.longt)
        print("latitude:",self.lat)

a=str(input("enter your city name"))
b= float(input("enter your longitude"))
c= float(input("enter your latitude"))

c1 = City(a,b,c)
c1.info()
