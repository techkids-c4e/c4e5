person=[{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]

def information(name):
    j=0
    for i in range(len(person)):
        if person[i]['full_name']==name:
            print(person[i]['full_name'],' teached: ',person[i]['session'],' salary: ',person[i]['rate'].replace('$',''))
            j=j+1
    if j==0:
        print('Do not find this full name, please input other full name')

x=str(input('Please input full_name: '))

information(x)


