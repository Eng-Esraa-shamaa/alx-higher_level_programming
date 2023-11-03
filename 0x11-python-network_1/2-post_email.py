#!/usr/bin/python3
"""
2. POST an email #0
"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    d = parse.urlencode({"email": argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], d) as p:
        print(p.read().decode('utf-8'))
