#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    cpy = my_list.copy()
    if (idx < 0):
        return cpy
    elif (idx > length):
        return cpy
    else:
        cpy[idx] = element
        return cpy
