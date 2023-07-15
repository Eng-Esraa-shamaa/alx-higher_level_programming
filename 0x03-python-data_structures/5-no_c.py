#!/usr/bin/python3
def no_c(my_string):
    new = my_string.translate({ord(j): None for j in 'cC'})
    return new
