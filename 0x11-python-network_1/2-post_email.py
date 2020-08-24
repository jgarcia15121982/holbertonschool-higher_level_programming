#!/usr/bin/python3
"""Python script that takes in a URL and an email,
   sends a POST request to the passed URL with the
   email as a parameter, and displays the body of
   the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    encoding = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], encoding) as req:
        print(req.read().decode('utf-8'))
