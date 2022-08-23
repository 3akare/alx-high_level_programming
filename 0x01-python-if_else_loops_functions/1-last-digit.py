#!/usr/bin/python3
from ast import Return
import random
number = random.randint(-10000, 10000)

if ((number % 10) == 0 or ((number * -1) % 10 == 0)):
    print(f"Last digit of {number} is {number % 10} and is 0")
elif (number % 10):
    if number >= 0:
        if ((number % 10) > 5):
            print(f"Last digit of {number} is {number % 10} and is\
 greater than 5")
        else:
            print(f"Last digit of {number} is {number % 10} and is\
 less than 6 and not 0")
    else:
        number *= -1
        print(f"Last digit of -{number} is -{number % 10} and is\
 less than 6 and\
 not 0")
else:
    print(f"Last digit of 0 is 0 and is 0")
