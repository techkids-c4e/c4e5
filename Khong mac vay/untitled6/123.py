from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, \
    ObjectProperty, StringProperty, ListProperty

from kivy.clock import Clock

size = 50
import listMap
positionPerson=listMap.positionPerson
# player=Players(positionPerson[0],positionPerson[1])
positionDoor=listMap.positionDoor
positionBox=listMap.positionBox
positionRock=listMap.positionRock
n=len(positionBox)

class Player(Widget):

    import Project
    px = NumericProperty(positionPerson[0]*size)
    py = NumericProperty(positionPerson[1]*size)
    # print(Project.positionPerson[0], Project.positionPerson[1])
    pos = ReferenceListProperty(px,py)
    image_ = StringProperty("nguoi.png")
    speedX = NumericProperty(0)
    speedY = NumericProperty(0)

    def de_check(self, box):
        c1 = (box.px == self.px + self.speedX)
        c2 = (box.py == self.py + self.speedY)
        if (c1 and c2 == True):
            return True
        else:
            return False

    def findBehindBox(self,box):

        n = -1

        c1 = (self.px + self.speedX == box.px)
        c2 = (self.py + self.speedY == box.py)

        if ((c1) and (c2)) == True:
            n = n+1
        return n

    # def check_Box_Rock(self,box,rock):
    #     n = self.findBehindBox(box)
    #     if n < 0:
    #         return True
    #     else:
    #         if box.checkRock() == True:
    #             return True
    #         else:
    #             False

    def checkRock(self,rock):
        c = True


        c1 = (self.px + self.speedX == rock.px)
        c2 = (self.py + self.speedY == rock.py)
        if ((c1) and (c2)) == True:
            c = c and False

        return c

    def moveBox(self, box):
        if self.de_check(box):
            box.px = box.px + self.speedX
            box.py = box.py + self.speedY

    def move(self):

        # c= self.checkRock(rock)
        # if(c==True):
        self.px += self.speedX
        self.py += self.speedY

    # def main_(self,rock,door,box):


class Box(Widget):

        # import Project

    import  Project
    px1 = Project.positionBox[0][0]
    py1 = Project.positionBox[0][1]
    #
    px = NumericProperty(px1*size)
    py = NumericProperty(py1*size)
    # pos = ReferenceListProperty(px,py)
    # image_ = StringProperty("")

    # print(Project.positionPerson[0], Project.positionPerson[1])

    pos =ReferenceListProperty(px,py)
    image_ = StringProperty("brick.jpg")

    def checkRock(self,rock,player):


        c1 = (self.px + player.speedX == rock.sx)
        c2 = (self.y + player.speedY == rock.y)
        if (c1 and c2 == True):
            c = c and False

class Door(Widget):

        # import Project

    import Project
    px1 = Project.positionDoor[0][0]
    py1 = Project.positionDoor[0][1]
    px = NumericProperty(px1*size)
    py = NumericProperty(py1*size)
    # print(Project.positionPerson[0], Project.positionPerson[1])
    pos = ReferenceListProperty(px,py)
    image_ = StringProperty("Door.png")




class Rock(Widget):
        # import Project

    for i in range(len(positionRock)):


        px1 = positionRock[i][0]
        py1 = positionRock[i][1]

        px = NumericProperty(px1 * size)
        py = NumericProperty(py1 * size)
        # print(Project.positionPerson[0], Project.positionPerson[1])
        pos = ReferenceListProperty(px, py)
        image_ = StringProperty("rock.png")







class SokobanGame(Widget):

    # import Project
    # listbox = Project.listBox


    # door = ObjectProperty(None)
    # box = ObjectProperty(None)
    # rock = ObjectProperty(None)
    #player = ObjectProperty(None)
    # box.draw()
    # listBox = ListProperty(listbox)
    # positionBox = Project.positionBox

    def drawBox(self):
        self.box.draw(100)



    def __init__(self, **kwargs):
        super(SokobanGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None



    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.player.speedX = 0
        self.player.speedY = 0
        if keycode[1] == 'left':
            self.player.speedX = -size
        elif keycode[1] == 'right':
            self.player.speedX = size
        elif keycode[1] == 'up':
            self.player.speedY = size
        elif keycode[1] == 'down':
            self.player.speedY = -size

        # for box in self.listBox:
        #     self.player.moveBox(self.box)
        self.player.moveBox(self.box)
        self.player.move()
        # self.box.draw()
        # self.drawBox()
        # self.player.main_(self.rock,self.door,self.box)

class SokobanApp(App):

    def build(self):
        game = SokobanGame()

        # game.box.draw()
        # Clock.schedule_interval(1.0 / 60.0)  # Vòng lặp fps game
        return game





if __name__ == "__main__":
    SokobanApp().run()
