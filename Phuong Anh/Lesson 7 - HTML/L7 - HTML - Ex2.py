print("Exercise 2: ")

import requests
unplash = requests.get("https://unsplash.com")

#save to computer
file_name = "unplash.html"
file_html = open(file_name, "wb")
file_html.write(unplash.content)
file_html.close()

#decode content
open_file = open(file_name, "rb")
decode_content = open_file.read().decode('utf-8')

from bs4 import BeautifulSoup
web_unplash = BeautifulSoup(decode_content, "html.parser")

#search by tag and attributes
img_tag = web_unplash.find_all("img", attrs={"class":"RIxWs"})
for img in img_tag:
    print(img.get("src"))
