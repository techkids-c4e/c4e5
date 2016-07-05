wave_1=[{"full_name":"Tran Quang Hiep",
         "class":"C4E",
         "rate":"$6.70",
         "session":17},

    {"full_name":"Nguyen Quang Huy",
     "class":"iOS",
     "rate":"$8.38",
     "session":18},

    {"full_name":"Nguyen Thanh Cuong",
     "class":"WEB",
     "rate":"$7.34",
     "session":19},

    {"full_name":"Ton Hong Duc",
     "class":"WEB",
     "rate":"$7.98",
     "session":18},

    {"full_name":"Tran Duc Hung",
     "class":"Android",
     "rate":"$5.62",
     "session":15}]
def read():
    name=str(input('Which one do you need to read? '))
    for x in wave_1:
        if name==x["full_name"]:
            print(x["full_name"],"teached: ",x["session"],"salary: ",x["rate"])
            break
        else:
            print('No information')
            break
def create():
    x=input("Please enter your information: ")
    x_list=x.split()
    wave_1.append({"full_name":x_list[0],
                   "session":x_list[1],
                   "rate":x_list[2]})
    print(x_list[0], "teached: ",x_list[1], "salary: ",x_list[2],"$")
def show_salary():
   name=input("Which one you want to know the total salary ? ")
   for y in wave_1:
      if name== y["full_name"]:
         if "$" in y["rate"]: #Nếu người dùng những tên có sẵn
            y["rate"]=y["rate"].replace('$','')
            total = float(y["session"])*float(y["rate"])
            print(name,"total salary is: ",total)
            break
         else: #Nếu người dùng chọn đúng tên vừa nhập lúc nãy
            total= float(y["session"])*float(y["rate"])
            print(name,"total salary is: ",total)
            break
def update_one():
   x=input("Please enter your information: ")
   x_list=x.split()
   for a in wave_1:
      if x_list[0] == a["full_name"]:
         wave_1.remove(a)
         wave_1.append({"full_name":x_list[0],
               "session":x_list[1],
               "rate":x_list[2]})
def delete():
   x=str(input('Which one do you need to delete ? '))
   for name in wave_1:
      if x == name["full_name"]:
         wave_1.remove(name)         
         print(x,'deleted')
         break
##      else:
##         print('error')
##         break 
while True:
    print('Hello, this is a salary program.')
    answer=str(input('Please, select your fuction (Create, Read, Read Salary, Update, Delete): '))
    if answer == "Create":#Nên tạo tên có 1 chữ để có thể update ở phần sau(Hiep 100 10)
        create()
    elif answer == "Read":
        read()
    elif answer == "Read Salary":
        show_salary()
    elif answer == "Update": #Hiện tại chương trình chỉ dùng được khi nhập tên có 1 chữ( VD: Hiep 100 10) 
        update_one()
    elif answer == "Delete":
        delete()
    else:
        print('Error')

