salary=[{"full_name":"Tran Quang Hiep","class":"C4E","rate":"6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"5.62","session":15}]

## WAVE 1.tinh luong
##for person in salary:
##    name = person['full_name']
##    session= int(person['session'])
##    rate=float(person['rate'])
##    total= classes*rate
##    print(name,' taught: ',classes,' salary: ',total)

## WAVE 2+3+4+5+6
def create():
    a=input('Please enter your information(name,class,rate,session): ').split(',')
    empty={'full_name':' ','class_':'','rate':'','session':''}#tao list rong, ep gtri,append
    empty['full_name']=a[0]
    empty['class_']=a[1]
    empty['rate']=a[2]
    empty['session']=a[3]
    salary.append(empty)
    total=int(a[2])*int(a[3])
    print(a[0],' taught ',a[3],' salary ',total)
    
def read():
    b=input('Whose salary do you wanna read? ')
    for person in salary:
        name = person['full_name']
        classes= int(person['session'])
        rate=float(person['rate'])
        total= classes*rate
        if name==b:
            print(b,' total salary is: ',total)
            
def update():
    c = input('Enter information you need to update : ').split(',')
    for person in salary:
        if person.get('full_name')==c[0]:
            person['session']=c[1]
            person['rate']=c[2]
    print('updated!')
    
def delete():
    d=input('who do you want to delete? ')
    for person in salary:
        if d in person.values():
            salary.remove(person)
    print(d,' deleted!')
    
while True:
    print('Hello, this is a salary program')
    n=input('Please select your function(create, read, update, delete) : ')
    if n=='create':
        create()
    elif n=='read':
        read()
    elif n=='update':
        update()
    elif n=='delete':
        delete()
