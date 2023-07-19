#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for el in a_dictionary:
            if el == key:
                a_dictionary[el] = value
    return a_dictionary
