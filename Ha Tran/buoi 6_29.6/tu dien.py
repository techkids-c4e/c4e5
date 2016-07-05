#Luu lai cac list: list cua list
#Ngoac nhon
#Ngan cach cac gia tri bang dau phay
#dictionary trong dictionary (dict in dict)
person={'name':'Ha',
        'favorite':'blue',
        'gender':'female'}

##print(person)
###override the key
##person['favorite']='black'
###print one key
##print(person['favorite'])
###delete a key(pop)
##...
for key,value in person.items():
    print(key,value)
    person.popitem('name'
