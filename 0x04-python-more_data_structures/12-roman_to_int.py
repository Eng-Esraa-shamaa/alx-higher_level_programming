#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or len(roman_string) == 0 or type(roman_string) != str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for i in reversed(roman_string):
        val = roman.get(i, 0)
        if val < prev:
            total = total - val
        else:
            total = total + val
        prev = val
    return total
