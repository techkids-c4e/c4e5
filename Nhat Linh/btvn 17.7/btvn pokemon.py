import requests
pokemon=requests.get("http://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pokémon)")
from bs4 import BeautifulSoup
trangweb_pokemon=BeautifulSoup(pokemon.content,"html.parser")
#name pokemon
name_pokemon=trangweb_pokemon.find("b")
print("Name Pokemon:", name_pokemon.get_text())
# pokemon image link
img_pokemon=trangweb_pokemon.find("img")
print("Pokemon Image Link:",img_pokemon.get("src"))
# pokemon code
code_pokemon=trangweb_pokemon.find("th",attrs={"width":"25%","class":"roundy","style":"background:#FFF;"})
code_pokemon1=code_pokemon.span
print("Pokemon Code:",code_pokemon1.get_text())
# Pokemon color
color_pokemon=trangweb_pokemon.find("td",attrs={"colspan":"4"})
color_pokemon1=color_pokemon.table["style"].split(":")[1]
color_pokemon2= color_pokemon1.split(";")[0]
print("Pokemon Color:",color_pokemon2)
