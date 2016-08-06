from bs4 import BeautifulSoup
import re
import requests
import json
import datetime
import UpdataMongo

Page_list=['33331950906'] #update bang tay
Dulieu = '?fields=posts.limit(2){shares,message,likes.summary(true),comments.summary(true)}&access_token='
Token = 'EAACEdEose0cBAD3zeS3IIYdnZBOZCYUdqB0OCJ9IDP5IOy2tAd9L9biHlsdZChyhBTogfyn0Fid1xDvYltQPjh47PYikZA7CM4me6VOrzE4ghDvhKCZCqgKrTAzvDjA1chRVbfIycvxmqBnfTg6mKRxsBxcEXe850WzbTo4CxgQZDZD'

JSON_list=[]

# Tao n duong link JSON cua n page
for i in Page_list:
    a=('https://graph.facebook.com/'+str(i)+Dulieu+Token)
    # print (re.sub('[\s+]','',a))
    JSON_list.append(a)





def getAndUp(data_dict):
    for i in data_dict["posts"]["data"]:
        postID = (i["id"])
        createTime = (i["created_time"])
        share = int((i["shares"]["count"]))
        like = int((i["likes"]["summary"]["total_count"]))
        comment = int((i["comments"]["summary"]["total_count"]))
        message = (i["message"])
        score = share + like + comment
        # print(score)
        updatetime = datetime.datetime.now()
        # print (updatetime)
        UpdataMongo.SavetoMongo(postID,message,score,updatetime)

def clawContent(fblink):
    facebook = requests.get(fblink)


    facebook_decoded = facebook.content.decode('utf-8')
    trangweb_facebook = BeautifulSoup(facebook_decoded,"html.parser")


    data_dict=json.loads(facebook_decoded)
    getAndUp(data_dict)

    nextpage = data_dict["posts"]["paging"]["next"]
    # print(nextpage)

    previouspage = data_dict["posts"]["paging"]["previous"]
    # print(previouspage)

    posts = []

# print(data_dict["posts"]["data"])

print(JSON_list)
for i in JSON_list:
    clawContent(i)

