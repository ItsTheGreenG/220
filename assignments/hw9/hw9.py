"""
Name: Owen Schlagenhaft
hw9.py

Problem: Hangman Gallows.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


import random
from graphics import *
#opening file
def get_words(file_name, list):
    in_file = open("words.txt", "r")
    words = in_file.readlines()
    return words
#creating a randomizer for list of words
def get_random_word(words):
    length = len(words)
    randomize = random.randint(0, length - 1)
    for i in range(len(words)):
        if i == randomize:
            secretword = words[i]
    return secretword
#creating if statement to search for letter in secret word
def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False
    pass
#checking to see if letter is in guesses
def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        guesses.append(letter)
        return False
    pass

#Creating secret word
def make_hidden_secret(secret_word, guesses):
    secret_word = secret_word.strip()
    # make hidden a list
    hidden = []
    for i in secret_word:
        if i in guesses:
            hidden.append(i)
        else:
            #append _ to end of word
            hidden.append("_ ")
    hidden = "".join(hidden)
    return hidden

    pass
def won(guessed):
   if "_ " in guessed:
       return False
   else:
       return True
   pass
# game runs correctly in terminal
def play_graphics(secret_word):
    #Creating window
    win = GraphWin("Hangman", 1000, 1000)
    win.getMouse()
    #Create stand for stick figure
    stand1 = Line(Point(500, 200), Point(500, 700))
    stand2 = Line(Point(475, 700), Point(525, 700))
    stand3 = Line(Point(475, 200), Point(525, 200))
    stand4 = Line(Point(475, 200), Point(475, 250))
    stand1.draw(win)
    stand2.draw(win)
    stand3.draw(win)
    stand4.draw(win)

    #Create Body
    head = Circle(Point(475, 250), 15)
    body = Line(Point(475, 500), Point(475, 300))
    arm1 = Line(Point(475, 260), Point(450, 275))
    arm2 = Line(Point(475, 260), Point(500, 245))
    leg1 = Line(Point(475, 300), Point(450, 325))
    leg2 = Line(Point(475, 300), Point(500, 325))
    #Put body in list for later use
    bodylist = [head, body, arm1, arm2, leg1, leg2]
    #creating for loop to cycle through guesses
    for i in range(1, 7, -1):
        textentry = Entry(Point(500, 750), 20)
        textbox = textentry.setText('Guesses')
        textbox.draw(win)
    #letters used
        guess = textentry.getText()
        guesstext = Text(Point(490, 500), "Letters Used: ")
        guesstext.draw(win)
        guessedletters = Text(Point(500, 500), guess)
        guessedletters.draw(win)


        if guess not in secret_word:
            for i in bodylist:
                drawing = bodylist[i]
                drawing.draw(win)
    play_command_line(secret_word)

    pass

words = []
l = get_words("words.txt", words)
secret_word = get_random_word(l)
guesses = []
# creating command line for game, checking wins, letters guessed, letter in secret word, and lives to assume win or not
def play_command_line(secret_word):
    lives = 6
    attempt = "_ "
    while not won(attempt):
        print("already guessed: ", guesses)
        print("guesses remaining: ", lives)
        print(make_hidden_secret(secret_word, guesses))
        letter = input("guess a letter: ")
        if already_guessed(letter, guesses):
            print("Try Again")
        if not letter_in_secret_word(letter, secret_word):
            lives = lives - 1
        if lives == 0:
            print("Game Over Hombre")
            print("The secret word was", secret_word)
            #didnt know how to stop, so used a break here
            break
        print(make_hidden_secret(secret_word, guesses))
        attempt = make_hidden_secret(secret_word,guesses)
        if won(attempt):
            print("You have Won!")


if __name__ == '__main__':
    play_command_line(secret_word)
    play_graphics(secret_word)
