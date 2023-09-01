#!/usr/bin/python3
"""
script take URL and email, send POST request to 
the passed URL with email as parameter, and
display body of response
"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    email = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], email)
    with request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
