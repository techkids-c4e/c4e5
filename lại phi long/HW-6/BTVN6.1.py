class City:
    def __init__(self, name, longt, lat):
        self.cityname = name
        self.citylongt = longt
        self.citylat = lat
    def Calculate_distance(self, city2):
        distance = ((self.citylongt-city2.citylongt)**2+(self.citylat-city2.citylat)**2)**0.5
        print (distance)
Hanoi = City( "hanoi", 50, 75)
Haiphong = City ( "haiphong", 25, 10)
x = Hanoi.Calculate_distance(Haiphong)

        
        
