def Craw_pokemon_data(link):
    import requests
    pokemon = requests.get(link)

    file_name = "pokemon.html"
    file_html = open(file_name,"wb")#write bin
    file_html.write(pokemon.content)
    file_html.close()

    from bs4 import BeautifulSoup
    trangweb_pokemon = BeautifulSoup(pokemon.content,"html.parser")

    bigfooter = trangweb_pokemon.find("td",attrs={"colspan":"4"})
    name = bigfooter.table.find("b")
    print(name.get_text())
    color = bigfooter.table.get("style").split(";")
    print(color[0])
    number = bigfooter.table.tr.th.find("span")
    print(number.get_text())
    image = trangweb_pokemon.find("td",attrs={"colspan":"6"})
    img = image.find("img")
    print(img.get("src"))


