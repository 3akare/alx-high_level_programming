#!/usr/bin/python3
'''Fetches https://alx-intranet.hbtn.io/status using request package
oppose to urllibs'''


import requests

with requests.get('https://alx-intranet.hbtn.io/status') as req:
    text = '''Body response:\n\t- type: {}\n\t- content: {}'''
    print(text.format(type(req.text), req.text))
