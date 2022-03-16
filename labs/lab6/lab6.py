from graphics import *
import math



# creating graphics box for input

def vigenere_graphic():
  win = GraphWin("Vigenere Cipher", 500, 500)
  Text(Point(75, 150), "Message to code").draw(win)
  Text(Point(75, 230), "Enter Keyword ").draw(win)
  Text(Point(250,350), "Resulting Message").draw(win)
  inputText = Entry(Point(280, 150), 30)
  inputText.setText("")
  inputText.draw(win)
  inputText2 = Entry(Point(280, 230), 20)
  inputText2.setText("")
  inputText2.draw(win)
  outputText = Text(Point(150, 150), " ")
  outputText.draw(win)
  button = Text(Point(220, 300), "Convert It ")
  Rectangle(Point(180,250), Point(280,320)).draw(win)
  win.getMouse()
  button.undraw()
  # Attempted Theory/Code for the encryption

  #Converting Input
  message = inputText.getText()
  keyword = inputText2.getText()
  keyword.upper()
  keyword.replace(" ", "")
  keywordlist = []
  message.upper()
  message.replace(" ", "")
  print(message)
  for message in keywordlist:
    Encription = (message + keyword) % 26
    print(Encription)


  win.getMouse()







vigenere_graphic()

#def cipher():

#cipher()