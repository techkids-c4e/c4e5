from mongoengine import*

connect('demo_connection',host = 'mongodb://techkids:codethechange@ds021751.mlab.com:21751/techkids')

class bangluong_huy(Document):
    name = StringField()
    rate = FloatField()
    session = StringField()
    class_ = StringField()

Hiep = bangluong_huy(name = "Hiep", class_ = "C4E", rate = "6.70", session = "17")
Huy = bangluong_huy(name  ="Huy", class_ = "iOS", rate = "8.38", session = "18")
Cuong = bangluong_huy(name = "Cuong", class_ = "WEB", rate = "7.34", session = "19")
Duc = bangluong_huy(name = "Duc", class_ = "WEB", rate = "7.98", session = "18")
Hung = bangluong_huy(name = "Hung", class_ = "Android", rate = "5.62", session = "15")

Hiep.save()
Huy.save()
Cuong.save()
Duc.save()
Hung.save()

list_ = []

for person in bangluong_huy.objects():
    list_.append(person)
    
def Creat():
    t = input("pls enter the information you want to add(Name/class/rate/session ): ")
    t = t.split(" ")
    info = bangluong_huy(name = t[0], class_ = t[1], rate = t[2], session = t[3])
    info.save()
    list_.append(info)
    print("Successfully created !")
    
def Read():
    for person in bangluong_huy.objects():
        print(person.name,"teach class",class_,session,"sessions ","with salary rate:",rate)
    
def Update():
    t = input("pls enter name and information you want to update(name/class/rate/session): ")
    t = t.split(" ")
    person = bangluong_huy.objects(name = t[0])
    person.class_ = t[1]
    person.rate = t[2]
    person.session = t[3]
    person.save()
    print("Updated !")
    
def Delete():
    t = input("Enter name of whom you want to delete from the list: ")
    for person in bangluong_huy.objects(name = t):
        person.delete()
    print("Delete process is completed !")
    
while True:
    t = input("What's your assignment? ")
    if t = "Creat":
        Creat()
    elif t = "Read":
        Read()
    elif t = "Update":
        Update()
    else:
        Delete()
