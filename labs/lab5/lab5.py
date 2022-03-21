
"""
Name: Owen Schlagenhaft
lab5.py
Created a group of functions to facilitate a number of mathematical and graphic based problems.
"""
from graphics import *
import math
def target():
    width = 500
    height = 500
    win = GraphWin("Target", width, height)
    win.redraw()
    center = Point(250,250)
    shape = Circle(center, 50)
    shape2 = Circle(center, 100)
    shape3 = Circle(center, 150)
    shape4 = Circle(center, 200)
    shape5 = Circle(center, 250)
    shape.setFill('Yellow')
    shape2.setFill('Red')
    shape3.setFill('Blue')
    shape4.setFill('Black')
    shape5.setFill('White')
    shape5.draw(win)
    shape4.draw(win)
    shape3.draw(win)
    shape2.draw(win)
    shape.draw(win)
    win.getMouse()
    win.close()



def triangle():
    width = 400
    height = 400
    win = GraphWin("Triangle", width, height)
    win.redraw()
    win.getMouse()
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    shape = Polygon(p1, p2, p3)
    shape.setFill('Red')
    y2 = p2.getY()
    x2 = p2.getX()
    x = p1.getX()
    y = p1.getY()
    print(y)
    print(y2)
    dx = x2 - x
    print(dx)
    dy = y2 - y

    print(dy)
    length = math.sqrt(dx ** 2 + dy ** 2)
    print(length)
    s = (dx + dy + length) / 2
    print(s)
    area = (s * (s - dx)*(s - dy)*(s - length)) ** .5
    print(area)

    perimeter = length + dx + dy
    label = Text(Point(200, 300), "Perimeter:")
    label2 = Text(Point(200, 320), perimeter)
    label3 = Text(Point(200, 350), "Area:")
    label4 = Text(Point(200, 370), format(area,'.2f'))
    label.draw(win)
    label2.draw(win)
    label3.draw(win)
    label4.draw(win)
    shape.draw(win)
    win.getMouse()

    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)










    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)


    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")



    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    inputText1 = Entry(Point(200, 240), 5).draw(win)
    inputText1.getText()
    outputText = Text(Point(200, 240), "").draw(win)
    inputText2 = Entry(Point(200, 270), 5).draw(win)
    inputText2.getText()
    inputText3 = Entry(Point(200, 300), 5).draw(win)
    inputText3.getText()
    win.getMouse()
    intr = int(inputText1)
    intg = int(inputText2)
    intb = int(inputText3)
    shape.setFill(color_rgb(intr, intg, intb))
    #Cannot figure how to apply the Color_rgb application to the function
    # Wait for another click to exit
    win.getMouse()
    #win.close()

def process_string():
    str1 = input("")
    print(str1[0])
    print(str1[-1])
    print(str1[1:5])
    print(str1[0]+str1[-1])
    print(10 * str1)
    for i in str1:
        print(i)
    len(str1)
    print(len(str1))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = (values[1] + values[3])
    print(x)
    x = (values[0] + values[2])
    print(x)
    x = (values[1] * 5)
    print(x)
    x = (values[2], values[3], values[4])
    print(x)
    x = (values[2], values[3], values[0] + values[2])
    print(x)
    x = [5, 2.5, 7.2]
    print(x)
    x = (x[0]+x[1]+x[2])
    print(x)
    x = len(values)
    print(x)

def another_series():
    sum = 0
    x = eval(input("Enter the number of terms:"))
    for i in range(0, 2*x, 2):
        n = (i % 6) + 2
        print(n, end=' ')
        sum = sum + n
    print("\n sum =", sum)



def main():
    target()
    triangle()
    color_shape()
    another_series()
    process_list()
    process_string()
    pass


main()






























