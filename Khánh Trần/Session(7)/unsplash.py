import requests
unsplash = requests.get("https://unsplash.com/")

file_name = "unsplash.html"
file_html = open(file_name,"wb")
file_html.write(unsplash.content)
file_html.close()

open_file = open(file_name,"rb")
decoded_ = open_file.read().decode('utf-8')

from bs4 import BeautifulSoup as bs
unsplash_ = bs(decoded_,"html.parser")

img_tags = unsplash_.find_all("img",attrs={"class":"cV68d"})
for img in img_tags:
    print(img.get("href"))


