"""
Name: Owen Schlagenhaft
hw6.py

Problem: multiple cipher and string problems

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math

def cash_converter():
    dollar = input("Enter an Integer:")
    dollar_format = int(dollar)
    dollar_decimal = "{:.2f}".format(dollar_format)
    print("That is $", dollar_decimal)



def encode():
    message = input("Enter a message:")
    key = input("Enter a key:")
    encryption = ""
    for i in range(len(message)):
        letters = ord(message[i]) - 65
        shift = ord(key[i % len(key)])-65
        applied_shift = shift + letters
        code = chr(applied_shift)
        encryption = encryption + applied_shift
    print(encryption)


def sphere_area(radius):
    surface_area = 4.0 * math.pi * radius**2.0
    return surface_area


def sphere_volume(radius):
    volume = (4.0/3.0) * math.pi * radius**3.0
    return volume


def sum_n(number):
    sum = (number*(number +1))/2
    return sum


def sum_n_cubes(number):
    sum = (number**2*(number+1)**2)/4
    return sum


def encode_better():
    message = input("Enter a message:")
    key = input("Enter a key:")
    encryption = ""
    for i in range(len(message)):
        letters = ord(message[i]) - 65
        shift = ord(key[i % len(key)])-65
        new_code = letters + shift
        rerun = new_code % 58
        character = rerun + 65
        new = chr(character)
        encryption = encryption + new
    print(encryption)


if __name__ == '__main__':
     cash_converter()
     encode()
     res = sphere_area(13)
     print(res)
     res = sphere_volume(13)
     print(res)
     res = sum_n(100)
     print(res)
     res = sum_n_cubes(13)
     print(res)
     encode_better()
pass
