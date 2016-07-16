import requests
unsplash = requests.get("https://unsplash.com/")
print(unsplash)

#save to comp de luu tru trang thai web 1 thoi diem nhat dinh
file_name='http://unsplash.com' # dat ten
file_html=open(file_name,'wb')#khoi tao file, wb: write bin
file_html.write(unplash.content)
file_html.close()
#decode content
open_file=open(file_name,'rb')#rb: read bin
decoded_content=open_file.read().decode('utf-8')# doc va decode

from bs4 import BeautifulSoup
trangweb_unsplash=BeautifulSoup(decoded_content,'html.parser')#parser: giup doc kieu du lieu, vd: text.parser


#search all image in articles section
img_tags=trangweb_unsplash.find_all('img')
for img_tag in img_tags:
    print(img_tag.get('src'))
