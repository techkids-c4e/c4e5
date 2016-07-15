class City():
    def __init__(self, name, longt, lat):
        self.name=name        
        self.longt=float(longt)
        self.lat=float(lat)
    def calcuateDistance(self,othercity):
        Distance=((self.longt-othercity.longt)^2+(self.lat-othercity.lat)^2)^(1/2)
        return(Distance)
    def get_data(self):
        self.name= input("Please, Enter your City name: ")
        self.longt= float(input("Please, Enter your City's longitude: "))
        self.lat=float(input("Please, Enter your City's latitude: "))
    def print_data(self):
        print("name: ", self.name)
#        print("longtitude: "+ str(self.longt))
#        print("latitude: "+ str(self.lat))
 ##Lỗi không gọi được str ở đây, không hiểu sao.       
import string     
        
print("Hello, This is City Distaince Calculate System")
list=[]
while True:
    try:
        action=int(input("""Chon chuc nang ban muon su dung:
1. Them thong tin thanh pho
2. Xem danh sach thang pho
3. Tinh khoang cach giua cac thanh pho
4. Exit
Nhap 1 so tu 1-4: """))
    except:
        print("Vui long nhap 1 so tu 1-4")
        
        
        
    if action==1:
        x=City(0,0,0)
        x.get_data()
        print("-----------------------")
        x.print_data()
##Get gia tri o doan nay cung loi luon
        (x.name).replace(" ","_") = a
        eval(a)=x
        list+=eval(a)
    if action==2:
        for i in list:
            print(i)
    if action==3:
        city1=input("Nhap thanh pho thu nhat: ")
        city2=input("Nhap thanh pho thu hai: ")
        distance=eval(city1).calcuteDistance(eval(city2))
        print("Khoang cach giua hai thanh pho ", city1, " va ", city2, " la: ", str(round(distance)))
    if action==4:
        print("Bye bye!!!")
        break
