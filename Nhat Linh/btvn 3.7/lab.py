#wave 1
data = [{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]
def read():
    name=input('Which one do you need to read? ')
    for i in data :
        if name==i["full_name"]:
            print(i["full_name"],'teached :',i["session"],"salary :",i["rate"])
read()

#wave 2
def add_data():
    x=input("Enter your information (name, session, rate)").split(" ")
    i={"full_name":x[0],"session":int(x[1]),"rate":float(x[2])}
    data.append(i)
add_data()
wave_1()

#wave 5
def Payroll(name) :
name=input('which one do you want to know the total salary of them: ')
    for x in data:
        if name == x["full_name"]: 
           total= x["session"]* float(x["rate"].split('$')[1])
           print(name, 'total salary is: ', total)
Payroll(name)

#wave 6
def update_one(): 
    x=input("Enter your information (name, session, rate)").split(" ")
    update={"full_name":x[0],"session":int(x[1]),"rate":float(x[2])}
    for i in data:
        if x[0]==i["full_name"]:
            data[i]=update
    print(x[0], x[1], x[2], "updated")
update_one()

#wave 7
def delete():
    x=input('Which one do you need to delete?')
    for i in data:
        if x==i["full_name"]:
            data.remove(i)
            print(data)
            print(x,"deleted")
delete()

#wave 8
print("Hello, this is a salary program.")
x= input("Please, select your fuction (Create,Read,Update,Delete): ")
if x == "Create":
    add_data()
elif x == "Read":
    read()
elif x == "Update":
    update_one()
else:
    delete()
    
