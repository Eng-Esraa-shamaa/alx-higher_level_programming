#!/usr/bin/python3
"""
8. Search API
"""

import requests
from sys import argv

if __name__ == "__main__":
    d = {"q": argv[1] if len(argv) > 1 else ""}
    request = requests.post("http://0.0.0.0:5000/search_user", data=d)
    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
