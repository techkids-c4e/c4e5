from pymongo import MongoClient

person=[{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]

def read():
    j=0
    name=str(input('Please input full_name: '))
    for i in range(len(person)):
        if person[i]['full_name']==name:
            print(person[i]['full_name'],' teached: ',person[i]['session'],' salary: ',person[i]['rate'].replace('$',''))
            j=j+1
    if j==0:
        print('Do not find this full name, please input other full name')

def creat():
    x=str(input('Please create your information ([name] [session] [salary/session]): '))
    y=x.split()
    y[2]=str('$'+y[2])
    z={'full_name':y[0],'session':y[1],'rate':y[2]}
    person.append(z)
    return (person)

def update():
    x=str(input('Please update your information ([name] [session] [salary/session]): '))
    y=x.split()
    y[2]=str('$'+y[2])
    z={'full_name':y[0],'session':y[1],'rate':y[2]}
    
    for i in person:
        if i['full_name']==z['full_name']:
            person[person.index(i)]=z
      
             
    return (person)

def delete():
    x=str(input('Please input person you want remove: '))
    for i in person:
        if i['full_name']==x:
            person.pop(person.index(i))
                               
    return (person)

print('Hello, this is a salary program.')
while True:

    i=str(input('Please, select your function (Creat, Read, Update, Detele): '))
    if i=='Creat':
        creat()
    if i=='Read':
        read()
    if i=='Update':
        update()
    if i=='Delete':
        delete()
