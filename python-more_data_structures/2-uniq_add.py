#!/usr/bin/python3
def uniq_add(my_list=[]):
    add, uniq = 0, set(my_list)
    for x in uniq:
        add += x
    return add
