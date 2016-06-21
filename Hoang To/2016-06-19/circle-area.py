import math
print ("welcome to circle area caculator :)")
repeat="Y"
while repeat.upper().strip()=="Y":
    radius=0
    while radius<=0:
        try:
            radius=float(input("Please enter radius of cicle: "))
            if radius<=0:
               print ("Radius must be possitive a number, please try again.") 
        except ValueError:
            print ("Radius must be possitive a number, please try again.")
    area=math.pi*radius**2
    print ("Area = " + str(round(area,2)))
    repeat=input("Y to caculate again, enter to exit: ")
print("Bye bye")
