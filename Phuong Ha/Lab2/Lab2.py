salary=[{"full_name":"Tran Quang Hiep","class":"C4E","rate":"6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"5.62","session":15}]
## Wave 1 : tinh luong
def tinh_luong():
    for person in salary:
        name = person['full_name']
        classes= int(person['session'])
        rate=float(person['rate'])
        total= classes*rate
        print(name,' teached: ',classes,' salary: ',total)
##        
# Wave 2 : add thong tin va in
n=input('Please enter your information: ').split(',')
empty={'full_name':' ','class':'','rate':'','session':''}
empty['full_name']=n[0]
empty['rate']=n[1]
empty['session']=n[2]
salary.append(empty)

tinh_luong()

# Wave 3: hien thi luong theo input ten nguoi
m=input('Ban muon hien thi luong cua ai? ')
def payroll():
    for person in salary:
        name = person['full_name']
        classes= int(person['session'])
        rate=float(person['rate'])
        total= classes*rate
        if name==m:
            print(m,' total salary is: ',total)
 
payroll()

# Wave 4:
import pymongo

