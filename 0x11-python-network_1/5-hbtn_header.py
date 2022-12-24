#!/usr/bin/python3
'''Takes in a URL, sends a request to the URL and displays the value
of the variable 'X-Request-Id' in the response header'''


import requests
import sys

with requests.get(sys.argv[1]) as req:
    print(req.headers.get('X-Request-Id'))
