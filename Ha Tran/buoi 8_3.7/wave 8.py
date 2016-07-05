list_=[{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]

def Read():
    for dict_ in list_:
        if dict_["full_name"]==name:
            print(dict_["full_name"],"teached:",dict_["session"], "salary",dict_["rate"])

def Create(a,b,c):
    x={"full_name":a,
       "session":b,
       "rate":c
       }
    list_.append(x)
    for dict_ in list_:
        if dict_["full_name"]==name:
            print(dict_["full_name"],"teached:",dict_["session"], "salary",dict_["rate"])

def Delete(name):
    for dict_ in list_:
        if dict_['full_name']==name:
            list_.remove(dict_)
            return list_

#wave 8
print('Hello, this is a salary program.')
while True:
    c=input('Please, select your function (Create,Read,Update,Delete:)')

    if c=='Create':
        name,session,rate=input('Please enter your information:').split(' ')
        Create(name,session,rate)
    elif c=='Read':
        name=input('Which one you want to know salary information?')
        Read()
    elif c=='Delete':
        name=input('Which one to you need to delete?')
        Delete(name)
        print(name,'deleted!')
