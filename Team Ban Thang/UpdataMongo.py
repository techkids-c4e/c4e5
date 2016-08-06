from mongoengine import *

connect('blog',host="mongodb://admin:admin@ds145415.mlab.com:45415/c4e5")

class PostData(Document):
    postID = StringField()
    msg = StringField()
    score = IntField()
    time = DateTimeField()

def SavetoMongo(postID, msg, score, time):
    postID = postID
    msg = msg
    score = score
    time = time
    data = PostData(postID = postID, msg = msg, score = score, time = time )
    data.save()


# for Post in PostData.objects():
#     print (Post.msg)
#


def searchByKey(keyword):
    # keyword = "a new attitude"
    related = PostData.objects(msg__contains = keyword).order_by("-score")[:3]
    list=[]
    for i in related:
        x = i.postID
        newID = x.split("_")[1] + "%26id%3D" + x.split("_")[0]
        list.append(newID)
    # print (list)
    return list

print(searchByKey("a new attitude"))

# ['33331950906_10154226316550907', '33331950906_10154226316550907']
