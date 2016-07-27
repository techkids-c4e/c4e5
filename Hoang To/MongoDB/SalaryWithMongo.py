from mongoengine import *

connect('blog', host='mongodb://techkids:codethechange@ds021751.mlab.com:21751/techkids')


class Hoang_To(Document):
    full_name = StringField()
    lop = StringField()
    rate = StringField()
    session = IntField()

# Insert raw data lan 1.
# salary = [{"full_name": "Tran Quang Hiep", "class": "C4E", "rate": "$6.70", "session": 17},
#           {"full_name": "Nguyen Quang Huy", "class": "iOS", "rate": "$8.38", "session": 18},
#           {"full_name": "Nguyen Thanh Cuong", "class": "WEB", "rate": "$7.34", "session": 19},
#           {"full_name": "Ton Hong Duc", "class": "WEB", "rate": "$7.98", "session": 18},
#           {"full_name": "Tran Duc Hung", "class": "Android", "rate": "$5.62", "session": 15}]
#
# for i in salary:
#     x = Hoang_To(i["full_name"], i["class"], i["rate"], i["session"])
#     x.save()
# for x in Hoang_To.objects:
#     print(x.full_name)



def tinh_luong(rate, session):
    s = float(rate.replace("$", "").strip()) * float(session)
    return (s)


def read(Hoang_To):
    name = input("Nhap ten nguoi ban muon tim: ").strip().lower()
    for i in Hoang_To.objects:
        c = 0
        if i.full_name.strip().lower() == name:
            luong = round(tinh_luong(i["rate"], i["session"]), 2)
            print(i.full_name + " teached: " + str(i["session"]) + " salary: " + str(luong))
            c = 1
            break
    if c == 0:
        print("Khong tim thay ban ghi ban yeu cau!")


def creat(Hoang_To):
    a, b, c, d = [i.strip() for i in
                  input("Hay nhap thong tin ban muon them (Ho va Ten, class, rate, session): ").split(",")]
    for i in Hoang_To.objects:
        u = 0
        if i.full_name == a:
            i.lop = b
            i.rate = c
            i.session = int(d)
            i.save()
            u = 1
            print("Da cap nhat ban ghi " + a)
            break
    if u == 0:
        d = Hoang_To(a, b, c, int(d))
        d.save()
        print("Da them moi ban ghi " + a)


def delete(Hoang_To):
    name = input("Nhap ten ban ghi muon xoa: ").strip()
    del_list=Hoang_To.objects(full_name=name)
    c = len(del_list)
    if c == 1:
        del_list[0].delete()
        print("Da xoa ban ghi: " + name)
    elif c == 0:
        print("Ban ghi muon xoa khong ton tai")





while True:
    print("Chuong trinh tinh luong tu dong: ")
    try:
        x = int(input("""
Vui long chon chuc nang ban muon su dung:
1. Read
2. Create/Update
3. Delete
4. Exit
"""))
    except:
        print("So khong hop le, vui long nhap lai")

    if x == 1:
        read(Hoang_To)
    elif x == 2:
        creat(Hoang_To)
    elif x == 3:
        delete(Hoang_To)
    elif x == 4:
        exit("Cam on ban da su dung chuong trinh")

    print("cam on da su dung chuong trinh")
