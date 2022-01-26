#Name: Owen Schlagenhaft
#lab2.py

#Problem: Calculating RMS, Harmonic, and Geometric Average

#Certification of Authenticity:
#I certify that this assignment is entirely my own work.




import math
def averagecalc():
    rms_Total = 0
    harmonic_Total = 0
    geometric_Total = 1
    values_Entered = eval(input("Enter the Values the be Entered: "))
    for i in range(0, values_Entered):
        value = eval(input("Enter the Number: "))
        rms_Total = value ** 2 + rms_Total
        harmonic_Total = (1 / value) + harmonic_Total
        geometric_Total = geometric_Total * value
    rms_average = rms_Total / values_Entered
    average2 = harmonic_Total / values_Entered
    rms_average = math.sqrt(rms_average)
    rms_average = round(rms_average, 3)
    harmonic_average = 1 / (harmonic_Total / values_Entered)
    geometric_average = geometric_Total ** (1.0 / values_Entered)
    geometric_average = round(geometric_average, 3)
    print(rms_average)

    print(harmonic_average)

    print(geometric_average)
averagecalc()










