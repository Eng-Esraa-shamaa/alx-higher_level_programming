#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dict = {}
    for i in a_dictionary:
        b_dict[i] = a_dictionary[i] * 2
    return b_dict
