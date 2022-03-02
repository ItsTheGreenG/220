"""Name: Owen Schlagenhaft
lab7.py
Problem: Bumper Cars!!!

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *
from time import sleep
from random import randint
import math
# creating a window
def window():
    width = 600
    height = 600
    win = GraphWin("Bumper Cars", width, height)
    width = win.getWidth()
    height = win.getHeight()
    radius = 20
    #assigning cars to variable and color
    car1 = Circle(Point(radius + 30, height/2),radius)
    car2 = Circle(Point(width - (radius + 30), height/2),radius)
    get_random_color(car1)
    get_random_color(car2)
    car1.draw(win)
    car2.draw(win)

    #couldnt figure out how to make the cars move.
    for i in range():
        car1.move(randint())
        car2.move(randint())


#creating random int function
def random(int_move_amt):
    return randint(-int_move_amt,int_move_amt)
# function to create random
def get_random_color(circle):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = color_rgb(r,g,b)
    return random_color
# collision Mathematics
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
        get_random_color(ball1)
        get_random_color(ball2)
    else:
        answer = False
    return answer
#defining the vertical boundaries for the cars
def hit_vertical(ball,win):
    ballCenter = ball.getCenter()
    radius = ball.getRadius()
    width = win.getWidth()
    ballxpos = ballCenter.getX()
    if ballxpos <= radius or ballxpos >= width-radius:
        answer = True
        get_random_color(ball)
    else:
        answer = False
    return answer

#ditto for horizontal
def hit_horizontal(ball,win):
    ballCenter = ball.getCenter()
    radius = ball.getRadius
    height = win.getHeight()
    ballypos = ballCenter.getY()
    if ballypos <= radius or ballypos >= height-radius:
        answer = True
        get_random_color(ball)
    else:
        answer = False
    return answer


# i dont understand how to call t
hit_horizontal()
hit_vertical()
did_collide()
get_random_color()
random()
    # i dont know why the functions arent calling....