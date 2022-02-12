"""
Name: Owen Schlagenhaft
hw4.py

Problem: Multiple tests on the usage of graphics and arithmetic

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""
import math
from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move Square")
    instructions.draw(win)

    # builds a circle
    shape_width = 50
    shape_height = 50
    shape = Rectangle(Point(100,100), Point(shape_width,shape_height))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        shape = Rectangle(Point(100, 100), Point(shape_width,shape_height))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)
    close = Text(Point(200, 350), "Click again to close")
    close.draw(win)
    win.getMouse()
    win.close()
squares()

def rectangle():
    peremeter = 0
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)
    num_clicks = 2
    for i in range(1):
        p1 = win.getMouse()
        p1.draw(win)
        p2 = win.getMouse()
        p2.draw(win)
        rect = Rectangle(p1, p2)
    rect.draw(win)
    y2 = p2.getY()
    x2 = p2.getX()
    x = p1.getX()
    y = p1.getY()
    width = x2 - x
    length = y2 - y
    peremeter = 2 * (length * width)
    area = length * width
    label2 = Text(Point(200, 300), "Peremeter")
    label2.draw(win)
    label = Text(Point(200, 315), peremeter)
    label.draw(win)
    label3 = Text(Point(200, 330), "Area")
    label3.draw(win)
    label4 = Text(Point(200, 345), area)
    label4.draw(win)
    label5 = Text(Point(200, 200), "Click again to close")
    label5.draw(win)
    win.getMouse()

rectangle()

def circle():
    bottom = 50, 50
    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    y2 = p2.getY()
    x2 = p2.getX()
    x = p1.getX()
    y = p1.getY()
    radius = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
    circ = Circle(Point(x, y), radius)
    circ.draw(win)
    text = Text(Point(200, 320), "Radius:")
    text.draw(win)
    text = Text(Point(200, 350), radius)
    text.draw(win)
    text2 = Text(Point(200, 200), "Click again to close")
    text2.draw(win)
    win.getMouse()
circle()

def pi2():
        pass

if __name__ == '__main__':
        pass