repeat="Y"
while repeat.upper().strip()=="Y":
	bacteria=-1
	time=-1
	while bacteria<0 or time<0:
		try:
			bacteria=int(input("Enter the initial number of bacteria: "))
			time=float(input("Enter the period of time by minutes: "))
		except ValueError:
			print("Number bacteria must be positive interger! \nPeriod of time must be positive number!")
		else:
			if bacteria<0 or time<0:
				print("Number bacteria must be positive interger! \nPeriod of time must be positive number!")
	total=bacteria*2**int(time//2)
	print (str.format("After {0} minutes we would have {1} bacterias",time,total))
	repeat=input("Y to caculate again, enter to exit: \n")