#!/usr/bin/python3
"""
4. What's my status? #1
"""

import requests


if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
