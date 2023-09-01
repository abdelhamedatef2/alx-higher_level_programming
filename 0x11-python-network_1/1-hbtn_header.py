#!/usr/bin/python3
"""
script take URL then send request and display
value of X-Request-Id var found in header
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
