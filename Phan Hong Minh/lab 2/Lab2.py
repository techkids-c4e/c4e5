salary = [{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]


#wave 1
##def calculate(rate, session):
##    total_salary = float(rate.replace("$", "")) * float(session)
##    return total_salary
##for person in salary:
##    print(person['full_name'], 'taught', person['session'], 'sessions, salary: ', calculate(person['rate'], person['session']))
    

#wave 2
def create():
    x=input('Please enter your information: ').split(" ")
    new={'full_name':x[0],
       'session':int(x[1]),
       'rate':int(x[2])}
    salary.append(new)
    print('Your information has been added')
    for person in salary:
        print(person)

#wave 5
def payroll():
        user_name = input('Please input your name: ')
        for person in salary:
            if user_name == person['full_name']:
                print (person['full_name'], "'s salary is", calculate(person['rate'], person['session']))

#wave 6
def update_info():
    x=input('Please enter your information: ').split(" ")
    updated_info = {'full_name': x,
                    'rate': z,
                    'session': t}
    for person in salary:
        if person['full_name'] == x[0]:
            person['session'] = int(x[1])
            person['rate'] = int(x[2])
            print('Your information has been updated')
        else:
            print( x[0], 'not found')
        print(person)

#wave7
def delete_info():
    user_name = input('Please input the name to be deleted: ')
    for person in salary:
        if user_name == person['full_name']:
            salary.remove(person)
            print('Information removed')
        else:
            print('No such information')
    print(person)


##wave 8
print("Hello, this is a salary program.")
b= str(input("Please, select your fuction (Create,Payroll,Update,Delete): "))
if b == "delete_info":
    delete_info()
elif b == "create":
    create()
elif b == "payroll":
    payroll()
else:
    update()


