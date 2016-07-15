import requests
unsplash =  requests.get("https://unsplash.com/")

file_name = "unsplash.html"
file_html = open (file_name,"wb")
file_html.write(unsplash.content)
file_html.close()

open_file = open(file_name,"rb")
decoded_content = open_file.read().decode('utf-8')

from bs4 import BeautifulSoup
web_unsplash = BeautifulSoup(decoded_content,"html.parser")

imgs_tags = web_unsplash.find_all("a",attrs={"class":"cV68d"})
for img_tag in imgs_tags:
    print(img_tag.get("href"))
