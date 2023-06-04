#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_argument = len(sys.argv) - 1
    if number_argument == 0:
        print("0 argument.")
    elif number_argument == 1:
        print("1 argument")
    else:
        print("{} arguments:".format(number_argument))
    for argument in range(1, number_argument + 1):
        print("{}: {}".format(argument, sys.argv[argument]))
