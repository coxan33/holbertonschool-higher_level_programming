#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = []
    for num in my_list:
        if num % 2 == 0:
            x.append(True)
        else:
            x.append(False)
        return x
