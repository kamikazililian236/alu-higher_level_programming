#!/usr/bin/python3
"""Sends POST request with a letter parameter and parses JSON response"""
import sys
import requests


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        res = r.json()
        if res:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
