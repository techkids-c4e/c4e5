#wave 1
list_=[{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]
name=input('Which one you want to know salary information?')
def Read():
    for dict_ in list_:
        if dict_["full_name"]==name:
            print(dict_["full_name"],"teached:",dict_["session"], "salary",dict_["rate"])
Read()

#wave 2
name,session,rate=input('Please enter your information:').split(' ')
def Create(a,b,c):
    x={"full_name":a,
       "session":b,
       "rate":c
       }
    list_.append(x)
    for dict_ in list_:
        if dict_["full_name"]==name:
            print(dict_["full_name"],"teached:",dict_["session"], "salary",dict_["rate"]) 
Create(name,session,rate)

#wave 5
name=input('Which one you want to know the total salary')
def Payroll(name):  
    for dict_ in list_:
        if dict_["full_name"]==name:
            total=float(dict_["rate"])*int(dict_["session"])
            return total
print(name, 'total salary is:', Payroll(name))

###wave 6
##import pymongo
##
##from pymongo import MongoClient
##from bson.objectid import ObjectId
##name,session,rate=input('Please enter your information:').split(' ')
##def Update(a,b,c):
##    client=MongoClient()
##    db=client.get_default_database
##    
##    list_=db.list
##    list_.update_one(
##        {"full name":a},
##        {$set:{"session":b,"rate":c}}
##        )
##    return list_
##Update(name,session,rate)
##print(name,'updated!)
#wave 7
name=input('Which one to you need to delete?')
def Delete(name):
    for dict_ in list_:
        if dict_['full_name']==name:
            list_.remove(dict_)
            return list_
Delete(name)
print(name,'deleted!')


