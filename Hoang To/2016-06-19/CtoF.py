print ("Celsius to Fahrenheit converter")
repeat="Y"
while repeat.upper().strip()=="Y":
	try:
		C=float(input("Please enter Celsius number \n"))
	except ValueError:
		print ("Celsius must be a number, please try again.")
	F=(C*1.8)+32
	print (str.format("{0} (C)= {1} (F)",C,F))
	repeat=input("Y to caculate again, enter to exit: ")
print("Bye bye")
