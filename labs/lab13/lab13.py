"""
Owen Schlagenhaft
lab13.py
This work is mine and mine only!
This is a program to create a trader alert program to make the money
"""
inputFileName = input("Enter name of input file: ")

def trade_alert(file_name):
    openedfile = open(inputFileName, 'r')
    readfile = openedfile.read()
    tradeslist = readfile.split(" ")

    count = 0
    for i in tradeslist:
        count = count + 1
        if i == 500:
            print("Alert trade volume at 500! Warning at : ", count, "seconds")
        elif int(i) >= 830:
            print("Warning Volume at or over 830! Warning at : ", count, "seconds")

trade_alert(inputFileName)