"""
Name: Owen Schlagenhaft
lab6.py

Problem: Attempted to create a Vigenere Cipher.

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""


from graphics import *
import math


def vigenere():
  width = 400
  height = 400
  win = GraphWin("Vigenere", width, height)
  win.setBackground("white")

  box_var = Entry(Point(230,120), 20)
  code = Text(Point(100, 100), "Message to Code")
  box_var.draw(win)
  code.draw(win)

  box_var_2 = Entry(Point(230, 120), 20)
  key = Text(Point(100,120), "Enter Keyword ")
  box_var_2.draw(win)
  key.draw(win)

  button = Rectangle(Point(150, 200), Point(250, 250))
  button.draw(win)
  code_par = Text(Point(200, 225), "Encode")
  code_par.draw(win)
  win.getMouse()
  button.undraw()
  code_par.undraw()
  text_var_key = box_var_2.getText()
  text_var_key = text_var_key.upper()
  text_var = box_var.getText()
  text_var = box_var.upper()
  text_var = text_var.replace(" ", "")

  empty_str = ""
  for i in range(len(text_var)):
    first = ord(text_var[i]) - 65
    shift = ord(text_var_key[i % len(text_var_key)]) - 65
    shift2 = (first + shift) % 26
    original = chr(shift2 + 65)
    empty_str = empty_str + original

    new_message = Text(Point(200,225), "Resulting message: " + empty_str)
    new_message.draw(win)


    close = Text(Point(200, 225), "Click to close window")
    close.draw(win)
    win.getMouse()
    win.close()

    if __name__ == '__main__':
      vigenere()



#def vigenere_graphic():
 # win = GraphWin("Vigenere Cipher", 500, 500)
  #Text(Point(75, 150), "Message to code").draw(win)
  #ext(Point(75, 230), "Enter Keyword ").draw(win)
  #Text(Point(250,350), "Resulting Message").draw(win)
  #inputText = Entry(Point(280,150), 30)
  #inputText = Entry(Point(280, 150), 30)
  #inputText.setText("")
  #inputText.draw(win)
  #inputText2 = Entry(Point(280,230), 20)
  #inputText2 = Entry(Point(280, 230), 20)
  ##inputText2.setText("")
  #inputText2.draw(win)
  #outputText = Text(Point(150, 150), " ")
  #outputText.draw(win)
  #button = Text(Point(220, 300), "Convert It ")
  #button.draw(win)
  #Rectangle(Point(180,250),Point(280,320)).draw(win)
  #Rectangle(Point(180,250), Point(280,320)).draw(win)
  #win.getMouse()
  #button.undraw()
  #Rectangle.undraw()
  # Attempted Theory/Code for the encryption

  #Converting Input
#  message = float(inputText.setText())
#  message = inputText.getText()
#  keyword = inputText2.getText()
#  keyword.upper()
#  keyword.replace(" ", "")
#  keywordlist = []
#  message.upper()
#  message.replace(" ", "")
#  print(message)
#  for message in keywordlist:
#    Encription = (message + keyword) % 26
#    print(Encription)


 # win.getMouse()




#vigenere_graphic()

#def cipher():

def cipher():
    message = input("Type Message Here")
    keyword = input("Insert Keyword Here")
    message.split(" ")
    keyword.split(" ")
    cipher1 = len(message) + len(keyword)
    print(cipher1)
cipher()
#cipher()