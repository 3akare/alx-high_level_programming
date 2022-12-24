#!/usr/bin/python3
'''Takes in URL, send a request to the URL and displays the value of
the X-Request-Id varibale found in the header of the response'''


import requests
import sys

with requests.get(sys.argv[1]) as req:
    print(req.headers.get('X-Request-Id'))
