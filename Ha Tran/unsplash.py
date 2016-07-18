import requests
unsplash = requests.get("https://unsplash.com/")
#print(unsplash)
file_name = "unsplash.html"
file_html = open(file_name,"wb")
file_html.write(unsplash.content)
file_html.close()

#decode_content:
open_file = open(file_name,"rb")

decoded_content = open_file.read().decode("utf-8")

#load vnexpress to BeautifulSoup
from bs4 import BeautifulSoup
trangweb_unsplash = BeautifulSoup(decoded_content,"html.parser")

#get needed information

tag_urls = trangweb_unsplash.find_all("a", attrs={"class":"cV68d"})
for tag_url in tag_urls:
    print("https://unsplash.com"+tag_url.get("href"))


