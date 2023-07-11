#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if (ord(ch) >= 97 and ord(ch) <= 122):
            m = ord(ch) - 32
            ch = chr(m)
        print("{}".format(ch), end="")
    print("{}".format(ch))
