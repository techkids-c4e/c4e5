import requests
vnexpress = requests.get("http://vnexpress.net")
#print(vnexpress)
file_name = "vnexpress.html"
file_html = open(file_name,"wb")
file_html.write(vnexpress.content)
file_html.close()

#decode_content:
open_file = open(file_name,"rb")
decoded_content = open_file.read().decode("utf-8")

#load vnexpress to BeautifulSoup
from bs4 import BeautifulSoup
trangweb_vnexpress = BeautifulSoup(decoded_content,"html.parser")

#get needed information

tag_texts = trangweb_vnexpress.find_all("div", attrs = {"class":"title_news"})
for tag_text in tag_texts:
    try:
        t = tag_text.find("a", attrs = {"class":"txt_link"})
        print(t.get("title"))
    except AttributeError:
        continue
