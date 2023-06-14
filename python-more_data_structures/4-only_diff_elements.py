#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    sets1, sets2 = list(set(set_1)), list(set(set_2))
    common = list(set(sets1).symmetric_difference(set(sets2)))
    return common
