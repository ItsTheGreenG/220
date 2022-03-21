"""
Name: Owen Schlagenhaft
hw8.py

Problem: Set of tasks to perform various For Loops and Boolean Statements

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
import math
from graphics import *

def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = 10 + nums[i]

    pass

def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    pass

def sum_list(nums):
    sum = 0
    for i in nums:
        sum = i + sum
    return sum
    pass


def to_numbers(nums):
    for i in range(0, len(nums)):
        nums[i] = int(nums[i])
        return nums

    pass


def sum_of_squares(nums):
    for i in range(0, len(nums)):
        nums[i] = int(nums[i])
        return nums
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            sum = 0
            for i in nums:
                sum = i + sum
            for i in range(0, len(nums[i])):
                nums = str(nums)
                return nums

    pass


def starter(weight, wins):

    if 150 <= weight < 160 and (wins >= 5):
        return True
    if weight > 199 or wins > 20:
        return True

    else:
        return False
    pass
print()

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            return False
        return False
    else:
        return False



def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_two = win.getMouse()
    circumference_point2 = win.getMouse()
    radius = math.sqrt(
        (center_two.getX() - circumference_point2.getX()) ** 2 + (
                center_two.getY() - circumference_point2.getY()) ** 2)

    circle_two = Circle(center, radius)
    circle_two.setFill("Pink")
    circle_two.draw(win)

    msgoverlap = Text(Point(5,4), "The Circles overlap")
    no_msoverlap =Text(Point(5,4), "The Circles do not overlap")
    msgclose = Text(Point(5,4), "Click to Close")

    if did_overlap(circle_one, circle_two):
        msgoverlap.draw(win)
        msgclose.draw(win)
    else:
        no_msoverlap.draw(win)
        msgclose.draw(win)
    win.getMouse()

def did_overlap(circle_one, circle_two):
    if circle_overlap(circle_one, circle_two):
        circle_one  circle_two or circle_one = circle_two
            return True

# having trouble calling the function in boolean
    pass


if __name__ == '__main__':
    pass
