import math
"""
Name: Owen Schlagenhaft
hw5.py

Problem: Solutions to problems using loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def name_reverse():
    full_name = input("Enter a name(first,last)")
    first, last = full_name.split()
    print(last, first)
name_reverse()

def company_name():
    website_name = input("Enter a Domain:")
    domain = website_name.split('.')
    print(domain[1])
company_name()

def initials():
    num_students = eval(input("How many students are in the class?"))
    for i in range(num_students):
        name = input(print("What is the name of Student", i + 1, "?"))
        first, last = name.split(' ')
        print(first[0] + last[0])
initials()

def names():
    list_names = input("Enter a list of names:")
    myList = list_names.split(',')
    for i in (myList):
        first, last = i.split()
        print(first[0]+last[0], end=' ')
names()

def thirds():
    total_sentences = eval(input("Enter the number of Sentences:"))
    nlist = []
    for i in range(total_sentences):
        sentence = input(print("Enter Sentence", i + 1))
        nlist.append(sentence)
    print(nlist)

    for j in nlist:
        print(j[::3],"\n")

thirds()

def word_average():
    sum = 0
    sentence = input("Enter a Sentence")
    myList = []
    myList = sentence.split()
    totalwords = len(myList)
    for i in myList:
        numletters = len(i)
        sum = numletters + sum
    average = sum / totalwords
    print(average)
word_average()

def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin:")
    words = sentence.split()
    for i in words:
        print(i[1:] + i[0] + "ay", end=" ")
pig_latin()