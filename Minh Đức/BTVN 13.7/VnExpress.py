import requests
vnex = requests.get("http://vnexpress.net/")
file_name = "vnexpress.html"
file_html = open(file_name,"wb")
file_html.write(vnex.content)
file_html.close()
open_file = open(file_name,"rb")
decoded_content = open_file.read().decode('utf-8')

from bs4 import BeautifulSoup
trangweb_vnex=BeautifulSoup(decoded_content,"html.parser")
x=trangweb_vnex.find("div", attrs={"class":"scroll-pane"})
print(x.get_text())

