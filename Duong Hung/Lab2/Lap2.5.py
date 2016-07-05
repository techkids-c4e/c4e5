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

def input_data(x):
    
    y=x.split()
    y[2]=str('$'+y[2])
    z={'full_name':y[0],'session':y[1],'rate':y[2]}
    person.append(z)
    return (person)

def salary(name):
    j=0
    for i in range(len(person)):
        if person[i]['full_name']==name:
            salary=float(person[i]['session'])*float(person[i]['rate'].replace('$',''))
            print(person[i]['full_name'],' total salary is: ',salary)
            j=j+1
    if j==0:
        print('Do not find this full name, please input other full name')

k=str(input('Please input your information ([name] [session] [salary/session]): '))
    
input_data(k)

x=str(input('Which one you want to know the total salary: '))

salary(x)
