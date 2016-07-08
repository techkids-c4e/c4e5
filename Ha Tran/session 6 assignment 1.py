#wave 1
hanoi = {"name" : "Hanoi",
         "longt" : 50,
         "lat" : 75}

haiduong = {"name" : "HaiDuong",
            "longt" : 25,
            "lat" : 10}
cities=[hanoi,haiduong]
class City:
    def __init__(self,name,longt,lat):
        self.n=name
        self.lo=longt
        self.la=lat

    def calculateDistance(self,city):
        distance=(((city["longt"]-self.lo)**2+(city["lat"]-self.la)**2)*0.5)
        print('The distance is: ',distance)


Hanoi=City(hanoi["name"],hanoi["longt"],hanoi["lat"])
Hanoi.calculateDistance(haiduong)
#wave 2

print('Hello, This is City Distance Caculate System.')
name=input('Please, Enter your City name:')
longt=input('Please, Enter your City’s longitude')
lat=input('Please, Enter your City’s latitude:')

print('Your City information is:\nname:',name,'\nlongitude:',longt,'\nlatitude:',lat)
            
new_city={"name":str(name),
          "longt":int(longt),
          "lat":int(lat)
          }
cities.append(new_city)

