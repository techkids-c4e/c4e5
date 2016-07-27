# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 00:43:06 2016

@author: Hoang To
"""


def tinh_luong(rate, session):
    s = float(rate.replace("$", "").strip()) * float(session)
    return (s)


def read(list):
    name = input("Nhap ten nguoi ban muon tim: ").strip().lower()
    for i in list:
        c = 0
        if i["full_name"].strip().lower() == name:
            luong = round(tinh_luong(i["rate"], i["session"]), 2)
            print(i["full_name"] + " teached: " + str(i["session"]) + " salary: " + str(luong))
            c = 1
            break
    if c == 0:
        print("Khong tim thay ban ghi ban yeu cau!")


def creat(list):
    a, b, c, d = [i.strip() for i in
                  input("Hay nhap thong tin ban muon them (Ho va Ten, class, rate, session): ").split(",")]
    for i in list:
        u = 0
        if i["full_name"] == a:
            i["class"] = b
            i["rate"] = c
            i["session"] = int(d)
            u = 1
            print("Da cap nhat ban ghi " + a)
            break
    if u == 0:
        d = {"full_name": a, "class": b, "rate": c, "session": d}
        list.append(d)
        print("Da them moi ban ghi " + a)


def delete(list):
    name = input("Nhap ten ban ghi muon xoa: ").strip()
    for i in list:
        c = 0
        if i["full_name"].lower() == name.lower():
            list.remove(i)
            c = 1
            print("Da xoa ban ghi: " + name)
    if c == 0:
        print("Ban ghi muon xoa khong ton tai")


salary = [{"full_name": "Tran Quang Hiep", "class": "C4E", "rate": "$6.70", "session": 17},
          {"full_name": "Nguyen Quang Huy", "class": "iOS", "rate": "$8.38", "session": 18},
          {"full_name": "Nguyen Thanh Cuong", "class": "WEB", "rate": "$7.34", "session": 19},
          {"full_name": "Ton Hong Duc", "class": "WEB", "rate": "$7.98", "session": 18},
          {"full_name": "Tran Duc Hung", "class": "Android", "rate": "$5.62", "session": 15}]

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
        read(salary)
    elif x == 2:
        creat(salary)
    elif x == 3:
        delete(salary)
    elif x == 4:
        exit("Cam on ban da su dung chuong trinh")

    print("cam on da su dung chuong trinh")
