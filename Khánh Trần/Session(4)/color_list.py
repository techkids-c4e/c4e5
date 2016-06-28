##Print out the color at index “i” in this list, “i” is entered by user

color_list = ["Blue", "Red", "Black", "Pink", "Brown", "Yellow"]
i = int(input("Enter a number from 0-5: "))
print("Your color: ",color_list[i])

##Print out all of the colors in the color list, in two ways

print(color_list)
for color in color_list:
    print(color)

##color look up
    
color = input("What's your favorite color? ")
i = color_list.index(color)
if i<=5:
    print("Your color is at index",i,"in my list")
else:
    print("Sorry, I could not find your color")
