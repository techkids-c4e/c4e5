import requests
vnexpress=requests.get('http://vnexpress.net/')
print(vnexpress)

file_name='vnexpress.html' 
file_html=open(file_name,'wb')
file_html.write(vnexpress.content)
file_html.close()

open_file=open(file_name,'rb')
decoded_content=open_file.read().decode('utf-8')

from bs4 import BeautifulSoup
trangweb_vnexpress=BeautifulSoup(decoded_content,'html.parser')

side_title=trangweb_vnexpress.find_all('div',attrs={'class':'scroll-pane'})
print(side_title)

