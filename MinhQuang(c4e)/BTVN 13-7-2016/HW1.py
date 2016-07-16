import requests
vnexpress = requests.get("https://vnexpress.net/")
print(vnexpress)
file_name = "vnexpress.html"
file_html = open(file_name, "wb")
file_html.write(vnexpress.content)
file_html.close()
decoded_content = open_file.read().decoded('utf-8')
from bs4 import beautifulsoup
trangweb_express = beautifulsoup(decoded_content, "html.parser")
print(trangweb_vnexpress.find("div", attrs = {"class":"scroll-pane"}))
                 
