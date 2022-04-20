"""
Owen Schlagenhaft

algorithms.py

creating high low game
"""

import math
from random import randint
list = [1,2,3,4,5]
def find_and_remove_first(list, value):
    name = "Owen Schlagenhaft"
    x = list.index(value)
    list[x] = name
    print(list)




def read_data(filename):
    in_file = open("data_sorted.txt", "r")
    words = in_file.readlines()
    return print(words)




def is_in_linear(search_val, values):
    if search_val in values:
        return True
    else:
        return False


def valid(x):
    if x <= 10 and x > 0:
        return True
    else:
        return False

def good_input():
    stuff = eval(input("Input a digit between 1 and 10: "))
    while valid(stuff) == False:
        stuff = eval(input("Try again... Input a digit between 1 and 10: "))
    if valid(stuff) == True:
        return stuff


def num_digits():
    things = eval(input("Please input a positive integer: "))
    count = 0
    while things != 0:
        things = things // 10
        count = count + 1
        print("The number of digits is " + str(count))
        things = eval(input("Please input a positive integer: "))


num_digits()





def correct(num, answer):
    if num == answer:
        return True
    else:
        return False


def hi_lo_game():
    user_guess = eval(input("Guess a number:"))
    guess = 1
    random_number = randint(1, 100)
    while user_guess != random_number and guess != 7:
        guess += 1
        if user_guess < random_number:
            print("too low")
        else:  # user_guess > random_number
            print("too high")
        user_guess = eval(input("guess the number: "))
        if user_guess == random_number:
            print("You won in " + str(guess) + " guesses!")
        if guess == 7:
            print("Sorry you lose. The number was " + str(random_number))
hi_lo_game()



def is_in_binary(search_val, values):
    if search_val in values:
        return True
    else:
        return False






