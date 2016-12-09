
i=1

with open(str(i) + ".txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

mapY=len(array)


mapX = 0
for i in range(mapY):
    l=len(array[i])
    mapX=max(mapX,l)

mapX=mapX-1



positionDoor=[]
positionBox=[]
positionRock=[]

for i in range(mapY):
    l=len(array[i])
    for j in range(l-1):
        if array[i][j] == ".":
            pD=[i,j]
            positionDoor.append(pD)

        if array[i][j] == "$":
            pB = [i, j]
            positionBox.append(pB)

        if array[i][j] == "#":
            pR = [i, j]
            positionRock.append(pR)

        if array[i][j] == "@":
            positionPerson = [i, j]


# print(positionDoor)
# print(positionBox)
# print(positionRock)


    # for j in range(len(array[i])):
    #     if