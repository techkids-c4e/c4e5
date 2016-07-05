def Create():
    a,b,c =  input("Please enter your infomation: ").split()
    x = {
       "full_name":a,
       "session":b,
       "rate":c
       }
    Salary.append(x)
    print(a,"teached:",b,"salary:",c)
def Read():
    d = str(input("Which one you want to know the total salary? "))
    for item in Salary:
        if d == item["full_name"]:
            total = float(item["session"]) * float(item["rate"])           
    print(d,"total salary is:",total)
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
    print(Salary)
    
Salary = [
          {"full_name":"Tran Quang Hiep","class":"C4E","rate":"6.70","session":17},
          {"full_name":"Nguyen Quang Huy","class":"iOS","rate":"8.38","session":18},
          {"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"7.34","session":19},
          {"full_name":"Ton Hong Duc","class":"WEB","rate":"7.98","session":18},
          {"full_name":"Tran Duc Hung","class":"Android","rate":"5.62","session":15}
         ]
print("Hello, this is a salary program.")
f = str(input("Please, select your fuction (Create,Read,Update,Delete): "))
if f == "Delete":
    Delete()
elif f == "Create":
    Create()
elif f == "Read":
    Read()
else:
    Update()
    
