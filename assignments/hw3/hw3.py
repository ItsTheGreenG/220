"""
Name: Owen Schlagenhaft
hw3.py

Problem: Solutions to problems using loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def average():
    totalgrades = 0
    grade = 0
    average = 0
    gradesentered = eval(input("How many grades are you entering?:"))
    for i in range(1, gradesentered + 1):
        grade = eval(input("Enter Grade:"))
        totalgrades = grade + totalgrades
    average = totalgrades / gradesentered
    print(average)
average()

def tip_jar():
    tiptotal = 0.0
    for i in range(1, 5 + 1):
        tip = (eval(input("How much would you like to tip?")))
        tiptotal = tip + tiptotal
    print("Your total Tips are:", tiptotal)
tip_jar()


def newton():
    approx = 0.0
    x = eval(input("What number do you want to square root?:"))
    approx = eval(input("How many times should we improve the approximation?:"))
    for i in range(0, approx + 1):
        approx = (approx + (x / approx)) / 2.0
    print("The square root is approximately:", approx)
#This one i had trouble getting the correct answer.... i do believe my arithmetic is wrong.
newton()

def sequence():
    termstotal = eval(input("How many terms would you like?:"))
    for i in range(1, termstotal + 1, 2):
        print(i,i, end='\t')
# cannot for the life of me figure out how to not print the final term twice.

sequence()

def pi():

# i dont really know what to say about this one. I was extremely perplexed. I'm probably missing something but i just don't know.

    if __name__ == '__main__':
        pass
