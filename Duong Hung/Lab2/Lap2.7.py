person=[{"full_name":"Tran Quang Hiep","class":"C4E","rate":"$6.70","session":17},
{"full_name":"Nguyen Quang Huy","class":"iOS","rate":"$8.38","session":18},
{"full_name":"Nguyen Thanh Cuong","class":"WEB","rate":"$7.34","session":19},
{"full_name":"Ton Hong Duc","class":"WEB","rate":"$7.98","session":18},
{"full_name":"Tran Duc Hung","class":"Android","rate":"$5.62","session":15}]



def delete(x):
    for i in person:
        if i['full_name']==x:
            person.pop(person.index(i))
                               
    return (person)

m=str(input('Please input person you want remove: '))
delete(m)
print(person)
