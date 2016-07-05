#Wave 1:
print('Wave 1:')
teacher_list = [{"Name":"Tran Quang Hiep","class":"C4E3","session number":"10","rate":"100","month salary":"1,000"},
                {"Name":"Nguyen Quang Huy","class":"C4E1","session number":"10","rate":"200","month salary":"2,000"},
                {"Name":"Tran Thu Ha","class":"C4E2","session number":"8","rate":"100","month salary":"800"},
                {"Name":"Nguyen Ha San","class":"Android","session number":"5","rate":"200","month salary":"1,000"},
                {"Name":"Nguyen Ha San","class":"iOS","session number":"8","rate":"100","month salary":"800"}]
for i in teacher_list:
    print(i["Name"], 'teached:', i["session number"], "salary:", i["month salary"]) #in gia tri trong list theo dang dict.

#Wave 2:
print('Wave 2:')
string = input("Please enter your information (Name, session number, rate): ")
a = string.split()
b = {"Name":a[0],
    "session number":a[1],
    "rate":a[2]}
teacher_list.append(b)
def data_extract(name, session, salary):
    print(b["Name"], 'teached:', b["session number"], "salary:", b["rate"])      
x = data_extract(b["Name"],b["session number"],b["rate"])

#Wave 5:
print("Wave 5")
input_name = input("Please enter teacher name: ")

def payroll(name):
    pay_roll = 'name not found'
    for i in teacher_list:
        if input_name == i["Name"]:
            pay_roll = int(i["session number"]) * int(i["rate"])
            break
    return pay_roll
         
print(payroll(input_name))


                            
