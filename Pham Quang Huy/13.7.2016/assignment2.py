import requests
unsplash = requests.get("https://unsplash.com/")
#print(vnexpress)
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
for link in trangweb_unsplash.find_all("a", attrs = {"class":"cV68d"}):
    t = link.get("style")
    t = t.split(")")[0].split("(")[1]
    print(t.replace('"',""))
    print()
