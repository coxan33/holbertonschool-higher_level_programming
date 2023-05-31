#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    div = number % 10
    number *= -1
    div *= -1
else:
    div = number % 10
if div > 5:
    print(f"Last digit of {number} is {div} and is greater than 5")
elif div == 0:
    print(f"Last digit of {number} is {div} and is 0")
elif div < 6 and div != 0:
    print(f"Last digit of {number} is {div} and is less than 6 and not 0")
