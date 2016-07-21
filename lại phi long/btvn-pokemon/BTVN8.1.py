import requests
pokemon = requests.get("http://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pokémon)")
print(pokemon)
file_name = "pokemon.html"
file_html = open(file_name, "wb")
file_html.write (pokemon.content)
file_html.close()
from bs4 import BeautifulSoup
trangweb_pokemon = BeautifulSoup(pokemon.content, "html.parser")

#name
namebox = trangweb_pokemon.find("big")
name_tag = namebox.big.b
pokemon_name = name_tag.get_text()
print("name: ",pokemon_name)
        
#image
image = trangweb_pokemon.find("a", attrs={"class":"image", "title": "Bulbasaur"})
Image = image.img
print("image link: ",Image.get("src"))

#code
number = trangweb_pokemon.find("th", attrs={"style":"background:#FFF;", "class":"roundy"})
sp = number.find("span")
print("pokemon's number:", sp.get_text())

#color
color = trangweb_pokemon.find("td", attrs={"colspan":"4"})
margin_color = color.table["style"].split(":")[1]
color_code = margin_color.split(";")[0]
print("background color code: ",color_code)
