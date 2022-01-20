"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area = ", area)


def calc_volume():
    length = eval(input("Enter the Length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the Height:"))
    volume = length * width * height
    print("volume =", volume)


def shooting_percentage():
    total_Shots = eval(input("Enter the Total Shots:"))
    shots_Made = eval(input("Enter the Shots Made:"))
    shot_Percentage = "{:.0%}".format(shots_Made / total_Shots)
    print("Shot Percentage =", shot_Percentage)


def coffee():
    pound_Total = eval(input("Enter how many pounds you would like:"))
    final_cost = (10.50 * pound_Total + .86 * pound_Total + 1.50)
    print("Your total is: =", final_cost)


def kilometers_to_miles():
    kilos = eval(input("How many Kilos did you travel?:"))
    miles = (kilos / 1.61)
    print("You traveled this many miles:", miles)


if __name__ == '__main__':
    pass
