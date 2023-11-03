#!/usr/bin/python3
"""
5. Response header value #1
"""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
