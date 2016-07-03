bang_luong= [{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
             {"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
             {"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
             {"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
             {"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]
for dictionary in bang_luong:
    print( dictionary["full_name"] ,' teached: ', dictionary["session"],' class: ', dictionary["class"],' rate: ', dictionary["rate"])
#wave 2
##emp_list= []
##x= input('Please enter your information name/session/rate: ').split( )
##i = { 'name': x[0],
##      'session': int(x[1]),
##      "rate": float(x[2])}
##print(i['name'], 'teached: ', i['session'], 'rate: ', i['rate'])
##emp_list.append(i)
#wave 5

a=input('which one do you want to know the total salary of them: ')
def Payroll(a) :
    for dictionary in bang_luong:
        rate_= dictionary["rate"].split("$")
##        int(rate_)
        if a== dictionary["full_name"]:
           luong= dictionary["session"]* rate_
           return luong
        
Payroll(a)
print (luong)
