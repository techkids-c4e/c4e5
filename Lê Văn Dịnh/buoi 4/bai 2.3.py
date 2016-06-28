number_list=["5","7","24","50","75","55","12","34"]
a=str(input("what is your name"))
print("Hello my name is",a,"and here is my flock")
print(number_list)
print("Now my biggest sheep has size",max(number_list),"let's shear it")
print('')
number_list.remove(max(number_list))
print("after shearing ,here is my flock")
print(number_list)

