import requests
unsplash = requests.get("https://unsplash.com/")
file_name ="unsplash.html"
file_html =open (file_name,"wb")
file_html.write (unsplash.content)
file_html.close()
open_file =open(file_name,"rb")
decoded_content = open_file.read().decode('utf-8')
from bs4 import BeautifulSoup
trangweb_unsplash = BeautifulSoup(decoded_content,"html.parser")
img_tags=trangweb_unsplash.find_all("a",attrs={"class":"cV68d"})
for img_tag in img_tags:
    print(img_tag.get("href"))
