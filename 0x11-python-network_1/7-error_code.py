#!/usr/bin/python3
'''Takes in a URL, sends a request to the URL and display the body of the response'''


import requests
import sys

if __name__ == '__main__':
    with requests.get(sys.argv[1]) as req:
        print(req.status_code)