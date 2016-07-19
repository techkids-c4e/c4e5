import requests
pokemon = requests.get("http://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)")
#print(pokemons)
file_name = "pokemon.html"
file_html = open(file_name,"wb")
file_html.write(pokemon.content)
file_html.close()

#decode_content:
open_file = open(file_name,"rb")

decoded_content = open_file.read().decode("utf-8")

#load pokemon to BeautifulSoup
from bs4 import BeautifulSoup
trangweb_pokemon = BeautifulSoup(decoded_content,"html.parser")
image = trangweb_pokemon.find("a", attrs={"class":"image"})
title=str(image.get("title"))
print(title)

code=trangweb_pokemon.find("th",attrs={"class":"roundy"})
print(code.find("span").string)

img=image.find("img",attrs={"width":"250"})
print(img.get("src"))

background=trangweb_pokemon.find("td",attrs={"colspan":"4"})
table=background.table
print(table.get("style").split(";")[0][11:19])

