import requests
from bs4 import BeautifulSoup

class pokemon:
    def init(self,link):
        pokemon = requests.get(link)
        soup = BeautifulSoup(pokemon.content,'html.parser')
        self.info = soup.find("table", attrs = {"class":"roundy"})
        
    def get_backgoundcolorcode(self):
        res = self.info.get("style")
        res = res.split("background: ")[1].split(";")[0]
        return(res)
    
    def get_img(self):
        res = self.info.find("img")
        return(res.get("src"))
        
    def get_name(self):
        info1 = self.info.find("td", attrs = {"width":"50%"})
        res = info1.big.big.b
        return(res.get_text())
        
    def get_code(self):
        info1 = self.info.find("th", attrs = {"class":"roundy"})
        res = info1.find("span").string
        return(res)
    
    def __init__(self, link):
        self.init(link)
        self.name = self.get_name()
        self.code = self.get_code()
        self.img =  self.get_img()
        self.bg_colorcode = self.get_backgoundcolorcode()

#bulbasaur = pokemon("http://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)")
pokemon_ = requests.get("http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number")
soup_ = BeautifulSoup(pokemon_.content,'html.parser')
listpokemon = soup_.find("table", attrs = {"style":"center", "style":"border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; border: 2px solid #FF1111; background: #FF1111;"})
listpokemon = soup_.find_all("tr")
count = 0
for pokemon in listpokemon:
    count = count + 1
    if count == 1 or count == 2: continue
    else:
        info = pokemon.find_all("td")
        
        res = info[3].a.get("href"))
        res = "http://bulbapedia.bulbagarden.net" + res
        pokemon__[count - 2] = pokemon(res)
        t = input()
    
##print(bulbasaur.img)
##print(bulbasaur.name)
##print(bulbasaur.code)
##print(bulbasaur.bg_colorcode)
