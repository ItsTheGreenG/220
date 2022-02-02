"""Name: Owen Schlagenhaft
lab3.py

Problem: creating a calculator for DOT to calculate road averages

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def traffic_average():
    cars = 0.0
    average = 0.0
    totalcars = 0.0
    overallsum = 0.0
    totalroads = eval(input("How many roads were surveyed?:"))
    for i in range(1, totalroads+1):
            days = eval(input("How many days was road " + str(i) + " surveyed?:"))
            for c in range(1, days + 1):
                cars = eval(input("How many cars passed on day " + str(c) + "?"))
                totalcars = cars + totalcars
                average = totalcars / days
            print("Road", i, "average vehicles per day:", average)
            overallsum = overallsum + totalcars
            totalcars = 0.0
    print("Total number of vehicles traveled on all roads:", overallsum)
    roadaverage = overallsum / totalroads
    roadaverage = round(roadaverage, 2)
    print(roadaverage)



 #       for j in range(totaldays):

 #           n = eval(input("How many days was road surveyed?:"))

 #           eval(input("How many cars passed on day 1?:"))


traffic_average()