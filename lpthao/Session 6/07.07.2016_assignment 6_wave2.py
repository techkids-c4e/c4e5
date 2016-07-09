class City:
    def __init__(self):
        self.name = ""
        self.longt = 0
        self.lat = 0
    def input(self):
        self.name = str(input("Enter your City name:"))
        self.longt = int(input("Enter your City's longt:"))
        self.lat = int(input("Enter your City's lat:"))
    def output(self):
        print("Your City information is:", self.name, self.longt, self.lat)

city = City()
print("Hello, This is City Distance Calculate System.")
city.input()
city.output()


        
    


