"""
Name: Owen Schlagenhaft
lab4.py

Problem: Creating a valentines day present

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import time
def valentine():
    width = 400
    height = 400
    win = GraphWin("Valentine",width, height)

    click = win.getMouse()
    P1 = Point(300, 170)
    P2 = Point(200, 300)
    P3 = Point(102, 170)
    p = Polygon(P1, P2, P3)
    p.draw(win)
    p.setFill('Red')
    p.setOutline('red')
    Center = Point(250, 160)
    circ = Circle(Center, 50)
    circ.setFill('red')
    circ.draw(win)
    Center = Point(152, 160)
    circ2 = Circle(Center, 50)
    circ2.setFill('red')
    circ.setOutline('red')
    circ2.setOutline('red')
    circ2.draw(win)
    label = Text(Point(200, 170), "Happy Valentines Day!")
    label.draw(win)
    for i in range(60,300):
        time.sleep(.01)
        line = Line(Point(60, 190), Point(340, 190))
        line.draw(win)
    # didn't end it since the user can exit out of the window.
    # had trouble attempting a spearpoint on the head of the line, so i kept it as is.
    click = win.getMouse()
valentine()



