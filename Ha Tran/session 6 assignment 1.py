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

