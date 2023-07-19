#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or len(roman_string) == 0 or type(roman_string) != str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = 0
    length = len(roman_string)
    for i in range(length):
        if i > 0 and roman[roman_string[i]] > roman[roman_string[i - 1]]:
            roman_num = roman[roman_string[i]] - 2 * \
                        roman[roman_string[i - 1]] + roman_num
        else:
            roman_num = roman[roman_string[i]] + roman_num
    return roman_num
