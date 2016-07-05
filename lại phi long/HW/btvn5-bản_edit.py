bang_luong= [{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
             {"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
             {"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
             {"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
             {"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]
##def Read():
##    for dictionary in bang_luong:
##        print( dictionary["full_name"] ,' teached: ', dictionary["session"],' class: ', dictionary["class"],' rate: ', dictionary["rate"])
#wave 2
def Create():

    x= input('Please enter your information name/session/rate/class: ').split(",")
    i = { 'name': x[0],
          'session': int(x[1]),
          "rate": float(x[2]),
          'class': str(x[3])}
    print(i['name'], 'teached: ', i['session'], 'rate: ', i['rate'])
    bang_luong.append(i)
Create()
print (bang_luong)
#wave 5

##a=input('which one do you want to know the total salary of them: ')
##def Payroll(b) :
##    for dictionary in bang_luong:
##        if b in dictionary["full_name"]: 
##           luong= dictionary["session"]* float(dictionary["rate"].split('$')[1])
##           print(b, 'total salary is: ', luong)
##        
##Payroll(a)
###wave 6
##information = input("Enter information you need to update: ").split(',')
##def  Update_one(information):
##    x = {"full_name"   :str(information[0]),
##         "class"       :str(information[1]),
##         "rate"        :str(information [2]),
##         "session"     :int(information[3])}
##    for dictionary in bang_luong:
##        if x["full_name"] in dictionary["full_name"]:
##            dictionary["full_name"] = x["full_name"]
##            dictionary["class"]= x["class"]
##            dictionary["rate"]=x["rate"]
##            dictionary["session"]= x["session"]
##Update_one(information)
##print (bang_luong)
##print("your information has been updated")
###wave 7
##name = input(' Which one do you want to delete? : ')
##def Delete(name):
##    for dictionary in bang_luong:
##        if name in dictionary["full_name"]:
##            bang_luong.remove(dictionary)
##Delete(name)
##print(bang_luong)
##print(name, 'has been deleted')
###wave 8
##print('this is a salary program')
##command= input("please, select your function: Read; Delete; Update")
##if command == " Read":
##    Read()
##elif command== "Delete":
##    name = input(' Which one do you want to delete? : ')
##    Delete(name)
##    print(name, 'has been deleted')
##elif command== "Update":
##    a = input("Enter information you need to update: ").split(" ")
##    Update_one(a)
##    print("your information has been updated")
##
