print("Exercise 1: ")

import requests
vnexpress = requests.get("http://vnexpress.net")

#save to computer
file_name = "vnexpress.html"
file_html = open(file_name, "wb")
file_html.write(vnexpress.content)
file_html.close()

#decode content
open_file = open(file_name, "rb")
decode_content = open_file.read().decode('utf-8')

from bs4 import BeautifulSoup
web_vnexpress = BeautifulSoup(decode_content, "html.parser")

#search by tag and attributes
news_list_tag = web_vnexpress.find_all("div", attrs={"class":"title_news"})
for news in news_list_tag:
    print(news.get_text()) #to get text
