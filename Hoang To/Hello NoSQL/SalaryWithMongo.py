from mongoengine import *

connect('hoang_to', host='mongodb://techkids:codethechange@ds021751.mlab.com:21751/techkids')


class Teacher(Document):
    full_name = StringField()
    lop = StringField()
    rate = StringField()
    session = NumberInt()


teacher = Teacher(full_name = 'Tran Quang Hiep', lop ='C4E', rate='$6.70', session = 17)
teacher.save()






# salary = [{"full_name": "Tran Quang Hiep", "class": "C4E", "rate": "$6.70", "session": 17},
#           {"full_name": "Nguyen Quang Huy", "class": "iOS", "rate": "$8.38", "session": 18},
#           {"full_name": "Nguyen Thanh Cuong", "class": "WEB", "rate": "$7.34", "session": 19},
#           {"full_name": "Ton Hong Duc", "class": "WEB", "rate": "$7.98", "session": 18},
#           {"full_name": "Tran Duc Hung", "class": "Android", "rate": "$5.62", "session": 15}]