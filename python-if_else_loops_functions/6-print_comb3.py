#!/usr/bin/python3
for number in range(10):
    for number2 in range(number + 1, 10):
        if number != 8 or number2 != 9:
            print("{:02d}, ".format(number * 10 + number2), end="")

print("89")
