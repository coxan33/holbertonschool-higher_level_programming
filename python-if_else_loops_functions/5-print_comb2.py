#!/usr/bin/python3
for numbers in range(0, 100):
    if (numbers < 10):
        print("0{},".format(numbers), end=" ")
    else:
        print("{}{}".format(numbers, (", " if numbers < 99 else "\n")), end="")
