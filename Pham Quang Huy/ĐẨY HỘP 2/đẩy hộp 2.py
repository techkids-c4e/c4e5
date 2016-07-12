a = [
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"]
    ]

def output_():
    for i in a:
        for j in i:
            print(j, end = " ")
        print()

class Character:
    def __init__(self, char, x, y):
        self.char = char
        self.x = x
        self.y = y
        a[y][x] = char
        self.speedX = 0
        self.speedY = 0

    def move(self):
        self.speedX = 0
        self.speedY = 0
        if s == "a" :
            self.speedX = -1
        if s == "d" :
            self.speedX = 1
        if s == "s" :
            self.speedY = 1
        if s == "w" :
            self.speedY = -1

    def draw(self):
        self.x = self.x + self.speedX
        self.y = self.y + self.speedY
        a[self.y][self.x] = self.char
        a[self.y - self.speedY][self.x - self.speedX] = "-"
        
    def checkboundery(self):
        t1 = self.x + self.speedX
        t2 = self.y + self.speedY
        if (t1 >= 0 ) and (t1 < 4) and (t2 >= 0) and (t2 < 5):
            return True
        else:
            return False

    def checkobstack(self, obstack):
        if a[self.y + self.speedY][self.x + self.speedX] == obstack.char:
            return True
        else:
            return False

    def findbox(self):
        for i in range(nBox):
            if box[i].x == self.x + self.speedX and box[i].y == self.y + self.speedY :
                return(i)
    
    def update(self):
        self.move()
        if (self.checkboundery() == True) and (self.checkobstack(door_) == False):
            if self.checkobstack(box_) == True:
                i = self.findbox()
                box[i].speedX = self.speedX
                box[i].speedY = self.speedY
                if box[i].checkboundery() == True:
                    if box[i].checkobstack(door_) == False:
                        box[i].draw()
                    elif box[i].checkobstack(door_):
                        global nBox
                        nBox = nBox - 1
                        box.pop(i)
                    self.draw()
            else:
                self.draw()

def checklost():
    for box_ in box:
        ##print(i, box[i].x, box[i].y)
        if ((box_.x == 0) and (box_.y == 0)) or ((box_.x == 0) and (box_.y == 4)) or ((box_.x == 3) and (box_.y == 0)) or ((box_.x == 3) and (box_.y == 4)):
            return 2
        else:
            return 0
    

P = input("Enter position of person (x, y): ").split(" ")
person = Character("P",int(P[0]),int(P[1]))

door = []
box = []

nDoor = int(input("Pls enter number of door: "))
for i in range(nDoor):
    D = input("Enter position of door (x, y): ").split(" ")
    door_ = Character("D",int(D[0]),int(D[1]))
    door.append(door_)

##print(len(door))

nBox = int(input("pls enter number of box: "))
for i in range(nBox):
    B = input("Enter position of the box(x, y): ").split(" ")
    box_ = Character("B",int(B[0]),int(B[1]))
    box.append(box_)
##print(len(box))
output_()

while True: #main loop
    if nBox == 0:
        print("You WIN !")
        break;
    else:
        if checklost() == 2:
            print("Sorry, You LOST!")
            break
    s = input()
    person.update()
    output_()
    
