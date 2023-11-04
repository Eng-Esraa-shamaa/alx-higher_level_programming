#!/usr/bin/python3
"""
0. What's my status? #0
"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    content = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode('utf-8')))
