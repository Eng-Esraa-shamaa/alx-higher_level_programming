#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (a < b):
        return (c)
    elif ((a > b) and (c > b)):
        return (a + b)
    elif ((a > b) and (b > c)):
        return ((a * b) - c)
