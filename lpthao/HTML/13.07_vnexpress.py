import requests
from bs4 import BeautifulSoup
vnexpress = requests.get("http://vnexpress.net")
file_name = "vnexpress.html"
file_html = open(file_name,"wb")
file_html.write(vnexpress.content)
file_html.close()
# Decode content
open_file = open(file_name,"rb")
decoded_content = open_file.read().decode("utf-8")
trangweb_vnexpress = BeautifulSoup(decoded_content,"html.parser")
# find titles
title_news = trangweb_vnexpress.find_all("div" , attrs={"class":"title_news"})
for title_news in title_news:
    title = title_news.find("a" , attrs = {"class" : "txt_link"})
    print(title.get("title"))

