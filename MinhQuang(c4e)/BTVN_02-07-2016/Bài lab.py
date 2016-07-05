list_1 =  [{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
        {"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
        {"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
        {"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
        {"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]
for x in list_1:
    print(x["full_name"],x["class"],x["rate"],x["session"])


list = []
y = str(input("please enter your information: "))
a = y.split(" ")
x = {"full_name"   :str(a[0]),
     "class"       :str(a[1]),
     "rate"        :int(a[2]),
     "session"     :int(a[3])}
print(x["full_name"],x["class"],x["rate"],x["session"])
list.append(x)


def Payroll(x):
    for item in list_1:
        if item["full_name"] == x:
            b = item["session"]*(item["rate"]
     return(b)
name = input("Which one you want to know the total salary? ")
b = Payroll(name)
print(name,"total salary is: ",b)


def  Update_1(y):
    a = y.split(" ")
    x = {"full_name"   :str(a[0]),
         "class"       :str(a[1]),
         "rate"        :int(a[2]),
         "session"     :int(a[3])}
     list.append(x)
a = input("Enter information you need to update; ")
Update_1(a)
print("your information has been updated")


def Delete(y):
    for item["name"] in list
        if item["name"] == y:
            list.remove(item)
    return(b)
name = input("Which one do you need to delete? ")
b = Delete(name)                                
print(name,"has been deleted")


def Read():
    for x in list_1:
        print(x["full_name"],x["class"],x["rate"],x["session"])
                                 
while True
    print("Hello, this is a salary program")
    m = input("please, select your fuction(Create,Read,Update,Delete): ")
    print(m)
    if m == "Read":
        Read()
    if m == "Update":
        a = input("Enter information you need to update: ")
        update_1
        print("Your information has been update")
    if m == "Deleted":
        name = input("Which one do you need to delete? ")
        b = Delete(name)                                
        print(name,"has been deleted")
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                
                                 
                                 
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  









                                  

                                  
 
