from graphics import *
from time import sleep
from random import randint
import math
def window():
width = 600
height = 600
win = GraphWin("Bumper Cars", width, height)
def random(int_move_amt):
    return randint(-int_move_amt,int_move_amt)
random()
def did_collide(ball1, ball2):
    ball1Center = ball1.getCenter()
    ball2Center = ball2.getCenter()
    ball1x1 = ball1Center.getX()
    ball1y1 = ball1Center.getY()
    ball2x1 = ball2Center.getX()
    ball2y1 =  ball2Center.getY()
    ball1Radius = ball1.getRadius()
    ball2Radius = ball2.getRadius()
    distance = (((ball2x1-ball1x1)**2)+ ((ball2y1-ball1y1)**2))**(1/2)
    radius = ball1Radius + ball2Radius
    if distance <= radius:
        answer = True
        randomColor(ball1)
        randomColor(ball2)
    else:
        answer = False
    return answer
did_collide()
window()