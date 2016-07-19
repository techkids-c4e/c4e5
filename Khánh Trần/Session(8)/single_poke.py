import requests
poke = requests.get("http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number")

file_name = "pokemon.html"
file_html = open(file_name,"wb")
file_html.write(poke.content)
file_html.close()

open_file = open(file_name,"rb")

from bs4 import BeautifulSoup as bs
poke_ = bs(open_file,"html.parser")

span = poke_.find("span",attrs={"id":"Generation_I"})
if (span["id"]) == "Generation_I":
    for i in range(250):
        
        #name
        table = poke_.find("table",attrs={"class":"roundy"})
        b = table.find("b")
        print("Pokemon name:",b.get_text())
        #code
        th = poke_.find("th",attrs={"class":"roundy"})
        span = th.find("span")
        print(" Index:",span.get_text())
        #pic
        a = table.find("img")
        print(" Photo link:",a.get("src"))
        #color
        td = poke_.find("td",attrs={"colspan":"4"})
        tablex = td.find("  table")
        color = tablex["style"].split()
        color1 = color[0].split(":")
        color2 = color1[1].split(";")
        print(" Mau vien:",color2[0])
        print("/n")



