
from mongoengine import*
connect('blog',host='mongodb://techkids:codethechange@ds021751.mlab.com:21751/techkids')#test : ten ket noi

class bangluong_Ha(Document):
    full_name=StringField()
    class_=StringField()
    rate=StringField()
    session=StringField()

Hiep = bangluong_Ha(full_name="Tran Quang Hiep",class_="C4E",rate="6.70",session='17')
Huy = bangluong_Ha(full_name="Nguyen Quang Huy",class_="iOS",rate="8.38",session='18')
Cuong = bangluong_Ha(full_name="Nguyen Thanh Cuong",class_="WEB",rate="7.34",session='19')
Duc = bangluong_Ha(full_name="Ton Hong Duc",class_="WEB",rate="7.98",session='18')
Hung= bangluong_Ha(full_name="Tran Duc Hung",class_="Android",rate="5.62",session='15')

Hiep.save()
Huy.save()
Cuong.save()
Duc.save()
Hung.save()

# truy xuat luong
for person in bangluong_Ha.objects:
    name = person.full_name
    classes= int(person.session)
    rate=float(person.rate)
    total= classes*rate
    print(name,' taught: ',classes,' salary: ',total)
#update
c = input('Enter information you need to update : ').split(',')
for person in bangluong_Ha.objects:
    if person.full_name==c[0]:
        person.session=c[1]
        person.rate=c[2]
print('updated!')

#delete
d=input('who do you want to delete? ')
for person in bangluong_Ha.objects:
    if d in person.values():
        bangluong_Ha.person.delete()
print(d,' deleted!')

