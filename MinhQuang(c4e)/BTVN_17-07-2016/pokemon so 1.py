import requests
pokemon = requests.get("http://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)")
print(pokemon)
pokemonimg = requests.get("http://bulbapedia.bulbagarden.net/wiki/File:001Bulbasaur.png")
print(pokemonimg)

file_name = "pokemon.html"
file_html = open(file_name, "wb")
file_html.write(pokemon.content)
file_html.close()

file_name_2 = "pokemonimg.html"
file_html_2 = open(file_name_2, "wb")
file_html_2.write(pokemonimg.content)
file_html_2.close()

from bs4 import BeautifulSoup
web_pokemon = BeautifulSoup(pokemon.content, "html.parser")
menu_bar = web_pokemon.find("td", class_= "roundy")
print(menu_bar.get_text())

pokemon_border = web_pokemon.find("td", attrs={"colspan":"4"})
margin = pokemon_border.table["style"].split(";")[0]
print(margin)

menu_bar_2 = web_pokemon.find("th", attrs={"style":"background:#FFF;", "class":"roundy"})
pokemon_number = menu_bar_2.find("span")
print(pokemon_number.get_text())
