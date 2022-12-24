#!/usr/bin/python3
''' Takes in URL, send a request to the URL and displays the value of
the X-Request-Id varibale found in the header of the response '''

import urllib.request
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        location = response.headers.__dict__.get('_headers')
        for i in location:
            if 'X-Request-Id' in list(i):
                print(i[1])
except Exception:
    pass


# Solution with request module
# import requests
# import sys

# with requests.get(sys.argv[1]) as req:
#     print(req.headers.get('X-Request-Id'))
