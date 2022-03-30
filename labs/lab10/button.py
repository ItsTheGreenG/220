from graphics import *
import math
class Button:
    shape = Rectangle(Point(100, 250), Point(150, 250))
    text = "Button"


    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        return self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX() and \
               self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY()

    def color_button(color):
        color.shape.setFill("red")
