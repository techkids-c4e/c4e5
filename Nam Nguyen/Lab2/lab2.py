list_luong=[{"full_name":"Tran Quang Hiep","class":"C4E","rate":"67","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"838","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]
## wave 1
##for dictionary in list_luong :
##      print(dictionary["full_name"],'teached: ',dictionary["session"],'class: ',dictionary["class"],'rate: ', dictionary["rate"])
##
## wave 2
def create():
    x=input('Please enter your information: ').split(" ")
    i={'name':x[0],
       'session':int(x[1]),
       'rate':int(x[2])}
    print(i['name'],' teached: ',i['session'], 'salary: ', i['rate'])

## wave 5
def Payroll():
    x= input("Which one you want to know the total salary ?")
    for y in list_luong:
          if x==(y["full_name"]):
                print(y["full_name"], "total salary is: ",int(y["rate"])*int(y["session"]))

    
##wave 6
def update():
    x=input('Enter infomation you need to update: ').split(" ")
    y=[{'name':x[0],
       'session':int(x[1]),
       'rate':int(x[2])}]
    list_luong.extend(y)
    print(x[0],"updated!")
    print(list_luong)

##wave 7
def delete():
    x=input('Which one do you need to delete ? ')
    for y in list_luong:
        if x==(y["full_name"]):
            list_luong.remove(y)
            print(x,"deleted!")
            print(list_luong)

##wave 8
print("Hello, this is a salary program.")
b= str(input("Please, select your fuction (Create,Payroll,Update,Delete): "))
if b == "delete":
    delete()
elif b == "create":
    create()
elif b == "Payroll":
    Payroll()
else:
    update()
