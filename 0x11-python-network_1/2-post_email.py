#!/usr/bin/python3
''' Takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and display the body of the
response (decoded in utf-8) '''


import urllib.request
import urllib.parse
import sys

values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(sys.argv[1]) as response:
    print(f'Your email is: {sys.argv[2]}')
