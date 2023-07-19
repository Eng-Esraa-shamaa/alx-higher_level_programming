#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0
    avg = 0
    div = 0
    for tupl in my_list:
        avg = (tupl[0] * tupl[1]) + avg
        div = tupl[1] + div
    total = float(avg / div)
    return total
