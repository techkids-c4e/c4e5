hanoi = {
    "name"  : "Hanoi",
    "longt" : 50,
    "lat"   : 75
    }

haiduong = {
    "name"  : "HaiDuong",
    "longt" :25,
    "lat"   :10
    }

class City :
    
    def __init__(obj1, city1):
        obj1.name = city1["name"]
        obj1.longt = city1["longt"]
        obj1.lat = city1["lat"]
        
    def calculateDistance(obj1,obj2):
        res = ((((obj1.longt - obj2.longt)**2+(obj1.lat - obj2.lat)**2)))**(1/2)
        return(res)

    def print(obj1):
        print("Your City information is: ")
        print("name:",obj1.name)
        print("longtitude:",obj1.longt)
        print("latitude:",obj1.lat)

Hanoi = City(hanoi)
Haiduong = City(haiduong)
x = Hanoi.calculateDistance(Haiduong)
print(x)
new_dict = {}
print("Hello, this is City Distance Calculate System.")
new_dict["name"] = input("Please, Enter your City name: ")
new_dict["longt"] = int(input("Please, Enter your City's longtitude: "))
new_dict["lat"] = int(input("Please, Enter your City's laatitude: "))

new_City = City(new_dict)
new_City.print()

        
