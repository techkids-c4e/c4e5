# Wave 1

list_1 = [{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]

for x in list_1 :
    print(x["full_name"],'teached :',x["session"],"salary :",x["rate"])

# Wave 2
list_ = []
string_ = input("Please enter your information: ")
a = string_.split(" ")
x =         {"name"     : a[0].title(),
             "session"  : int(a[1]),
             "rate"     : int(a[2])}
print(x["name"],'teached :',x["session"],"salary :",x["rate"])
list_.append(x)

# Wave 5
def Payroll(x):
    res = -1
    for item in list_:
        if item["name"] == x :
            res = item["rate"] * item["session"]
            break;
    return res

name = input("Which one you want to know the total salary ? ")
name = name.lower()
name = name.title()
res = Payroll(name);
if res >= 0 :
    print(name,"total salary is:",res)
else :
    print(name,"not found")

# Wave 6
def update_one(string_):
    a = string_.split(" ")
    a[0] = a[0].lower()
    x =     {"name"     : a[0].title(),
             "session"  : int(a[1]),
             "rate"     : int(a[2])}
    list_.append(x)

a = input("Enter infomation you need to update: ")
update_one(a)
print("Your information has been updated")

# Wave 7

def delete(string_):
    res = False
    for item in list_:
        if item["name"] == string_ :
            list_.remove(item)
            res = True
    return(res)

name = input("Which one do you need to delete ? ")
name = name.lower()
name = name.title()
res = delete(name)
if res == True :
    print(name,'has been deleted !')
else :
    print(name,"not found")

# Wave 8 : Full program

def Read():
    for item in list_:
        print(item["name"],"teached :",item["session"],"salary :",item["rate"])

print("Hello, this is a salary program.")
while True:
    command = input("select your function (Creat, Read, Update, Delete): ")
    command = command.strip()
    command = command.lower()
    if command == "read" :
        Read()
    elif command == "update" :
        a = input("Enter infomation you need to update: ")
        update_one(a)
        print("Your information has been updated") 
    elif command == "delete" :
        name = input("Which one do you need to delete ? ")
        name = name.lower()
        name = name.title()
        res = delete(name)
        if res == True :
            print(name,'has been deleted !')
        else :
            print(name,"not found")      
        

            
    




    



