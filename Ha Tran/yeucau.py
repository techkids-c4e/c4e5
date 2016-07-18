import requests
tinhte = requests.get('https://tinhte.vn/')
print(tinhte)
#print(tinhte.content)
file_name="tinhte.html"
file_html= open(file_name,"wb")
file_html.write(tinhte.content)
file_html.close()
open_file=open(file_name,"rb")
decoded_content=open_file.read().decode('utf-8')
from bs4 import BeautifulSoup
trangweb_tinhte=BeautifulSoup(decoded_content,"html.parser")
##print(trangweb_tinhte.get_text())
print(trangweb_tinhte.find('title'))
print(trangweb_tinhte.find('div',attrs={'id':'copyright'}))
#find all tags
img_tags=trangweb_tinhte.find_all("img",attrs={"class":"bbCodeImage LbImage"})
#return a list of tags
for img_tag in img_tags:
    print(img_tag.get("title"))
heading_tags=trangweb_tinhte.find_all("h2",attrs={"class":"subHeading"})
for heading_tag in heading_tags:
    print(heading_tag.get_text())
