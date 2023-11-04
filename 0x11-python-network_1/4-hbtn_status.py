#!/usr/bin/python3
"""
4. What's my status? #1
"""

import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    t = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
