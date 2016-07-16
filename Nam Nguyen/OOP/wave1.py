##class calculateDistance:
##    def __init__(self):
##        self.hanoi = {"name" : "Hanoi","longt" : 50,"lat" : 75}
##        self.haiduong = {"name" : "HaiDuong","longt" : 25,"lat" : 10}
##    def print(self):
##        print("The distance is",(((self.hanoi["longt"])-(self.haiduong["longt"]))**2+((self.hanoi["lat"])-(self.haiduong["lat"]))**2)**(1/2))
##        (self.hanoi["longt"])
##l=calculateDistance()
##l.print()

##wave 2:
##class calculateDistance: 
##    def __init__(self,x,y,z):
##        self.city = x
##        self.longitude = y
##        self.latitude = z
##    def print(self):
##        print("Name: ",self.city)
##        print("Longitude: ",self.longitude)
##        print("Latitude: ",self.latitude)
##print("Hello, This is City Distance Caculate System.")
##l=calculateDistance(x=input("Please, Enter your City name: "),y=input("Please, Enter your City’s longitude: "),z=input("Please, Enter your City’s latitude: "))
##l.print()


#option 1
##class VendingMachine:
##    def __init__(self, coin, button):
##        self.manufacturer = coin
##        self.year = button
##        if button==1:
##            if coin>7:
##                print("Cam lay Coke di may` va", coin-7,"K tien thua")
##            if coin==7:
##                print("Cam lay Coke di may`")
##            elif coin < 7:
##                print("Khong du tien dâu")
##        if button==2:
##            if coin>10:
##                print("Cam lay Enegry di may` va", coin-10,"K tien thua")
##            if coin==10:
##                print("Cam lay Enegry di may`")
##            elif coin < 10:
##                print("Khong du tien dâu")
##        if button==3:
##            if coin>5:
##                print("Cam lay Water di may` va", coin-5,"K tien thua")
##            if coin==5:
##                print("Cam lay Water di may`")
##            elif coin < 5:
##                print("Khong du tien dâu")
##    def print(self):
##        print("Bye Qúy Khách")
##print("Welcome To Vending Machine")
##print("Coke:7K")
##print("Enegry:10K")
##print("Water:5K")
##p = VendingMachine(5,3)
##p.print()


