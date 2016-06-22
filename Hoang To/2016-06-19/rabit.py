mature=0
newborn=1
conclusion=""
for x in range(8):
	total=mature+newborn #total number of rabit
	newborn=mature       #newborn this month
	mature=total         #Total mature at end this month
	conclusion+=str.format("Month {0}: {1} pair(s) of rabbits \n",x,total)
print (conclusion)
