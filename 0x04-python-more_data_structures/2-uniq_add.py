#!/usr/bin/python3
def uniq_add(my_list=[]):
    newSet = set(my_list)
    total = 0
    for i in newSet:
        total = total + i
    return total
