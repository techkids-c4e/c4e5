from mongoengine import *
connect('btvn-long', host ='mongodb://techkids:codethechange@ds021751.mlab.com:21751/techkids')

class bang_luong_philong(Document):
    full_name = StringField()
    rate = FloatField()
    session = StringField()
    class_teaching = StringField()

Hiep = bang_luong_philong(full_name="Tran Quang Hiep",class_teaching="C4E",rate="6.70",session="17")
Huy = bang_luong_philong(full_name="Nguyen Quang Huy",class_teaching="iOS",rate="8.38",session="18")
Cuong = bang_luong_philong(full_name="Nguyen Thanh Cuong",class_teaching="WEB",rate="7.34",session="19")
Duc = bang_luong_philong(full_name="Ton Hong Duc",class_teaching="WEB",rate="7.98",session="18")
Hung = bang_luong_philong(full_name="Tran Duc Hung",class_teaching="Android",rate="5.62",session="15")

Hiep.save()
Huy.save()
Cuong.save()
Duc.save()
Hung.save()

#truy xuat
for person in bang_luong_philong.objects():
    name = person.full_name
    class_teaching = person.class_teaching
    rate = person.rate
    session = person.session
    print(name, " teached ", session, " in class", class_teaching, " rate ", rate)
