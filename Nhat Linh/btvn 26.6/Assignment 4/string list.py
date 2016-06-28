#1.1
my_color_list=["blue","red","black","pink","brown","yellow"]
print(my_color_list)
#1.2
print("color_list at index 3:", my_color_list[3])
#1.3
x=int(input('enter a number from 0-5'))
print('Your color', my_color_list[x])
#1.4
print(my_color_list)
for x in my_color_list:
    print(x)
#1.5
x=input('What is your favorite color')
y=my_color_list.index(x)
if x in my_color_list:
    print("your color is at index",y,"in my list")
