import requests
vnexpress =  requests.get("http://vnexpress.net")

file_name = "vnexpress.html"
file_html = open (file_name,"wb")
file_html.write(vnexpress.content)
file_html.close()

open_file = open(file_name,"rb")
decoded_content = open_file.read().decode('utf-8')

from bs4 import BeautifulSoup
trangweb_vnexpress = BeautifulSoup(decoded_content,"html.parser")

title_tags = trangweb_vnexpress.find_all("div",attrs={"class":"content_scoller width_common"})
for title_tag in title_tags:
    print(title_tag.get_text())
