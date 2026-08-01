#!/usr/bin/python3
"""Uses Basic Auth to retrieve and print a user's GitHub ID"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    try:
        res = r.json()
        print(res.get('id'))
    except ValueError:
        print("None")
