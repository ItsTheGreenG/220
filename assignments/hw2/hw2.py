"""
Name: <Owen Schlagenhaft>
hw2.py

Problem: Multitude of math problems working with for loops and working around .pow and other math functions

Certification of Authenticity:

I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upperbound = eval(input("What is your Upperbound? : "))
    total = 0
    for x in range(0, upperbound + 1):
        if x % 3 == 0:
            total = total + x
    print(total)
sum_of_threes()

def multiplication_table():
    for i in range(1,11):
        for j in range(1,11):
            print(i * j, end='\t')
        print('')
multiplication_table()


def triangle_area():
    area = 1
    side_a = eval(input("Enter the first side:"))
    side_b = eval(input("Enter the second side:"))
    side_c = eval(input("Enter the third side:"))
    semi_p = (side_a + side_b + side_c) / 2
    area = (semi_p * (semi_p - side_a) * (semi_p - side_b) * (semi_p - side_c))
    math.sqrt(area)
    area = round(area, 3)
    int(area, 10)
    print("Your area is:", area)

triangle_area()


def sum_squares():
    sum = 0
    lowerbound = eval(input("What is your Lower bound?"))
    upperbound = eval(input("What is your Upper bound?"))
    for i in range(lowerbound, upperbound + 1):
        sum = i * i + sum
    print(sum)

sum_squares()

def power():

    base = eval(input("What is your Base?"))
    exponent = eval(input("What is your Exponent?"))
    s = base
    for i in range(1, exponent):
        s = s * base
    print(base, "^", exponent, "=", s)

power()

if __name__ == '__main__':
    pass
