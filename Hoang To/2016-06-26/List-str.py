colorlist=["Blue","Green","Black","White","Grey"]

print("My color list")
print(colorlist)
print("colorlist at index 3: ", colorlist[3])

i=int(input("input a number 0-4: "))
print("Your color: ",colorlist[i])

for x in colorlist:
	print(x)

a=input("What's favorite color? ")
try:
	y=colorlist.index(a)
	print("Your color is at index ",str(y)," in my list")
except ValueError:
	print("Sorry, I could not find your color")