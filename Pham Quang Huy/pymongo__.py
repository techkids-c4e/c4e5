import pymongo

# Config MongoDB

uri = "mongodb://admin:admin@ds119598.mlab.com:19598/cafeteria"

client = pymongo.MongoClient(uri)

db = client.get_default_database()

# Get MENU collection


menu_items = db["menu"].find()

menu_items_length = db["menu"].count()


# Get ORDER collection

order_item = db["order"].find()

order_item_length = db["order"].count()

menu = {}
order = list()

# clone PRICE and ORDER

for i in range(menu_items_length):
##    print(menu_items[i])
    menu[menu_items[i]["name"]] = menu_items[i]["price"]

for i in range(order_item_length):
    
    order.append(order_item[i])

#print(order)
def Order(food):
    return(menu[food.capitalize()])

# Ordering
for customer in order:
    bill = 0
    name = customer["customer"]
    
    for food in customer["order"]:
        bill += Order(food)
    print("customer {0}: {1} $".format(name, bill))

