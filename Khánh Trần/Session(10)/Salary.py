from mongoengine import *
connect('blog',host='mongodb://techkids:codethechange@ds021751.mlab.com:21751/techkids')
class Salary(Document):
    full_name = StringField()
    rate = StringField()
    session = StringField()

    def Create():
        a,b,c =  input("Please enter your infomation: ").split(",")

        p = Salary(a,b,c)
        p.save()
        print(a,"teached:",c,"salary rate:",b)
    def Read():
        d = input("Which one you want to know the total salary? ")
        for item in Salary:
            if d == item["full_name"]:
                total = float(item["session"]) * float(item["rate"])           
        print(d,"total salary is:",total,"$")
    def Update():
        a,b,c =  input("Please enter your infomation: ").split()
        for item in Salary:
            if a == item["full_name"]:
                item["session"] = b
                item["rate"] = c
        print("Updated!")
    def Delete():
        e = str(input("Which one do you need to delete? "))
        for item in Salary:
            if e == item["full_name"]:
                Salary.remove(item)
        print("finished!")

print("Hello, this is a salary program.")
while 1:
    f = str(input("Please, select your fuction (Create,Read,Update,Delete): "))
    if f == "Delete":
        Salary.Delete()
    elif f == "Create":
        Salary.Create()
    elif f == "Read":
        Salary.Read()
    else:
        Salary.Update()



    
