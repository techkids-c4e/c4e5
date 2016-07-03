sheepsize=[8,39,59,20,300,500,399]

print("Hello, my name is Hoang an there are my ship sizes")
print(sheepsize)
print("")

save=0
r=3
for i in range(1,r+1):
	print("MONTH ",str(i),":")
	sheepsize=[x+50 for x in sheepsize]
	print("One month has passed, now here my flock")
	print(sheepsize)
	m=max(sheepsize)
	save+=(m-8)
	n=sheepsize.index(m)
	sheepsize[n]=8
	print("Now my biggest sheep has size ",str(m)," let shear it")
	print("After shear it here my flock")
	print(sheepsize)
	print("")
total=sum(sheepsize)
money=total*2
smoney=save*2
print("My flock has size in total :",str(total))
print("I would get ",str(total)," *2$ = ",str(money),"$")
print("And after ",str(r)," month I have save ",str(smoney)) 
#doc nham de bai, no viet roi thi thoi cu de day