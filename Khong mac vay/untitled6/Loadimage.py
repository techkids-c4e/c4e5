import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout


class DrawingSpace(RelativeLayout):
    t = 10
    def move(self):
        self.t = self.t + 10


class ExampleApp(App):
    # x_ = 20
    # y_ = 20
    def build(self):
        Rec = DrawingSpace()
        for i in range(2):
            Rec.move()

if __name__ == "__main__":
    ExampleApp().run()
