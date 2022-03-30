from graphics import *

class Door:
    shape = Rectangle(Point(50,50),Point(250,250))
    text = "Door"
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)
        self.secret = True

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

    def open(color, label):
        color.shape.setFill()

    def close(color, label):
        color.shape.setFill()

    def color_door(color):
        color.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        else:
            return False
    def set_secret(secret):
        secret = 2

