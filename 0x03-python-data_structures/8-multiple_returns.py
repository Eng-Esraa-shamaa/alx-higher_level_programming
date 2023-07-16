#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    new_tuple = ()
    if (length == 0):
        new_tuple = (0, "None")
    else:
        new_tuple = (length, sentence[0])
    return new_tuple
