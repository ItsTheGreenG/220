"""
Name: Owen Schlagenhaft
lab10.py

Problem: Door Game

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""

from graphics import *
import math
from door import Door
from button import Button


def main():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)
    button1 = Button(Rectangle(Point(50, 50), Point(300, 150)), "Exit")
    button1.draw(win)
    door1 = Door(Rectangle(Point(50, 150), Point(300, 350)), "Closed")
    door1.draw(win)
    win.getMouse()
    door1.color_door("red")

main()