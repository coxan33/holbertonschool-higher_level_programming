#!/usr/bin/python3
def common_elements(set_1, set_2):
    sets1, sets2, common = list(set(set_1)), list(set(set_2)), []
    for x in range(len(sets1)):
        for y in range(len(sets2)):
            if sets1[x] == sets2[y]:
                common.append(sets1[x])
    return common
