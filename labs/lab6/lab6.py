from graphics import *






"""def vigenere_graphic():
  win = GraphWin("Vigenere Cipher", 500, 500)
  Text(Point(75, 150), "Message to code").draw(win)
  Text(Point(75, 230), "Enter Keyword ").draw(win)
  Text(Point(250,350), "Resulting Message").draw(win)
  inputText = Entry(Point(280,150), 30)
  inputText.setText("")
  inputText.draw(win)
  inputText2 = Entry(Point(280,230), 20)
  inputText2.setText("")
  inputText2.draw(win)
  outputText = Text(Point(150, 150), " ")
  outputText.draw(win)
  button = Text(Point(220, 300), "Convert It ")
  button.draw(win)
  Rectangle(Point(180,250),Point(280,320)).draw(win)
  win.getMouse()
  button.undraw()
  #Rectangle.undraw()

  #Converting Input

  message = float(inputText.setText())
  print(message)




  win.getMouse()







vigenere_graphic()"""

def cipher():
    message = input("Type Message Here")
    keyword = input("Insert Keyword Here")
    message.split(" ")
    keyword.split(" ")
    cipher1 = len(message) + len(keyword)
    print(cipher1)
cipher()