#!/usr/bin/python3
def remove_char_at(str, n):
    for ch in str:
        str2 = str[:n] + str[n+1:]
        return (str2)
    if n < 0:
        return (str)
