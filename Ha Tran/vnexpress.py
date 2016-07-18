import requests
from bs4 import BeautifulSoup
vne=requests.get('http://vnexpress.net/')
##print(vne)
file_name='vne.html'
file_html=open(file_name,'wb')
file_html.write(vne.content)
file_html.close()
open_file=open(file_name,"rb")
decoded_content=open_file.read().decode('utf-8')
vnexpress=BeautifulSoup(decoded_content,"html.parser")

title_new=vnexpress.find('div',attrs={'class':'scroll-pane'})
print(title_new.get_text())
