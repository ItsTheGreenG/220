import math
"""
Name: Owen Schlagenhaft
lab8.py

Problem: Creating a weighted average calc for a Wacky Grader.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""






def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name)
    students = in_file.readlines()
    #splitting name from numbers
    for i in students:
        fullname, numbers = i.split(": ")
        numbers = numbers.split(" ")
        weight = numbers[::2]
        grades = numbers[1::2]
        weighttotal = 0
        weightedavg = 0
        classaverage = 0
        # creating weight and grade as an int
        for i in range(0, len(weight)):
            weight[i] = int(weight[i])
        for i in range(0, len(grades)):
            grades[i] = int(grades[i])
        # counting weight
        for i in weight:
            weighttotal = i + weighttotal
        # creating if statement for the average to provide an error or not
        if weighttotal == 100:
            print()
            classaverage = weighttotal + classaverage
        elif weighttotal < 100:
            print()
        elif weighttotal > 100:
            print()

        #looking in the length of the weight to create the weighted avg.
        for i in range(0, len(weight)):
            assignment = weight[i] * grades[i]
            weightedavg = assignment + weightedavg
        weightedavg = weightedavg / 100
        print(weightedavg)
weighted_average("grades.txt","")

def main():
    open("grades.txt", "r")
    open("avg.txt", "w")
    average = eval()
    average.write("avg.txt")


    #main()

