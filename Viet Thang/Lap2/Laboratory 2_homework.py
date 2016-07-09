#wave1
data = [{"name":"Tran Quang Hiep","class":"C4E","rate":"6.70","session":17},
        {"name":"Nguyen Quang Huy","class":"iOS","rate":"8.38","session":18},
        {"name":"Nguyen Thanh Cuong","class":"WEB","rate":"7.34","session":19},
        {"name":"Ton Hong Duc","class":"WEB","rate":"7.98","session":18},
        {"name":"Tran Duc Hung","class":"Android","rate":"5.62","session":15}]

for i in data:
    print(i["name"],'teached:',i["session"],'rate:',i["rate"])

#wave2
dulieumoi = input('Nhap du lieu moi (Name, session, rate): ')
a = dulieumoi.split()
b = {"name":a[0],
    "session":a[1],
    "rate":a[2]}
data.append(b)
def tachdulieu(name, session, rate):
    print(b["name"], 'teached:', b["session"],'rate:', b["rate"],'$')
x = tachdulieu(b["name"],b["session"],b["rate"]) #tai sao xoa di code lai khong chay?


#Wave5
nhapten=str(input('Which one you want to know the total salary ?'))

def Payroll(nhapten):
    for i in data:
        if nhapten == i["name"]:
            salary = float(i["rate"])*i["session"]
    return salary

##salary = str('notfound')
Payroll(nhapten)
print(Payroll(nhapten))

