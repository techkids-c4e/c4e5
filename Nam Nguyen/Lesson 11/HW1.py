import requests
vnexpress = requests.get("http://vnexpress.net/")
print(vnexpress)
#print(vnexpress.content)
file_name = "vnexpress.html"
file_html = open  (file_name,"wb")
file_html.write(vnexpress.content)
file_html.close()
#decode content
open_file = open(file_name,"rb")
decoded_content = open_file.read().decode('utf-8')

#load vnexpress.net to BeautifulSoup
from bs4 import BeautifulSoup
trangweb_vnexpress = BeautifulSoup(decoded_content,"html.parser")
#print(trangweb_tinhte.get_text())
#lay tieu de
##print(trangweb_vnexpress.find("title"))

#lay noi dung class="scroll-pane"
print(trangweb_vnexpress.find("div",attrs={"class":"scroll-pane"}))

