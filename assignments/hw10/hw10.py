"""
Owen Schlagenhaft
hw10.py

completing problems without for loops

"""

def fibonacci(n):
    num1, num2 = 1, 1
    sequence = []
    count = 0
    while count < n and n > 1:
        sequence.append(num1)
        answer = num1 + num2
        num1 = num2
        num2 = answer
        count += 1
    return sequence[n -1]
    fibonacci()

def double_investment(principle,rate):
    while principle <
    annual = principle(1 + rate)
    double_investment()


def syracuse(int):
    output = [int]
    while int != 1:
        if int % 2 == 0:
            int = int / 2
            output.append(int)
        elif int % 2 != 0:
            int = 3 * int * 1
            output.append(int)
    return output
syracuse(int)
def goldback():
    goldback()

