from mongoengine import *
connect('blog', host =' mongodb://<dbuser>:<dbpassword>@ds139425.mlab.com:39425/laiphilong') #blog-ten ket noi

class c4e5(Document):
    author= StringField()
    title= StringField()

##post1 = c4e5(author= "long", title= "xin chao")
##post1.save


###truy suat tat ca du lieu
##for post in c4e5.objects():
##    print(post.author)
##print("done")
##
###truy suat du lieu cu the
##for post in c4e5.objects(author="Huy"):
##    print(post.author)
##print("done")

###xoa du lieu
##mylist = c4e5.objects(author="Long")
##for i in mylist:
##    print(i.author)
##mylist[0].delete()
##print("sau khi da xoa")
##mylist = c4e5.objects(author="Long")
##for i in mylist:
##    print(i.author)

#ghi de gia tri
long=c4e5("long","xin chao")
long.title="xin chao edited"
long.save()
for i in c4e5.objects(author="long"):
    print(c4e5.objects(author="long")[0].title)
