# WAVE 1
list_ = [
    {"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
    {"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
    {"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
    {"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
    {"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]

for item in list_ :
    print(item["full_name"],'teached :',item["session"],"salary :",item["rate"])

# WAVE 2

def Creat(string_):
    a = string_.split(" ")
    t = '';
    for i in range(len(a)- 2):
        t = t + ' ' + a[i]
    t.title()
    x =         {"full_name": t.strip(),
                 "rate"     : a[len(a) - 1],
                 "session"  : int(a[len(a) - 2])}
    list_.append(x)
    
string_ = input("Please enter your information: ")
Creat(string_)

def Get_(a):
    b = a.split(" ")
    return b[len(b)].title

# WAVE 5
def Payroll(x):
    res = -1
    
    for item in list_:
        if Get_(x) = Get_(item["name"]) :
            res = float(item["rate"].split(0)) * item["session"]
            break
    return res

name = input("Which one you want to know the total salary ? ")
res = Payroll(name)
if res >= 0 :
    print(name, "total salary is:",res)
else :
    print("Name not found")
    
# WAVE 6
def update_one():
    string_ = input("Enter name of person that you want to update")
    res = False;
    a = string_.split(" ")
    t = '';
    for i in range(len(a)- 2):
        t = t + ' ' + a[i]
    t = t.title()
    t = t.strip()
    for item in list_:
        if t = item["name"]:
            class_ = input("Which class you want to update (rate, session)")
            class_ = class_.strip()
                print("Current value of",class_,"is",item[class_])
                t = ("Enter new value you want to adjust")
                if class_ == "session" :
                    t = int(t)
                item[class_] = t;
            res = True;
            print("updated !")
            break
    if res == False:
        print("name not found!")
        
update_one()

# WAVE 7

def delete(string_):
    res = False
    for item 


    
            


