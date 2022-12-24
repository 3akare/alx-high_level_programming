#!/usr/bin/python3
'''Takes in a letter and sends a POST requestr to http://0.0.0.0:5000/search_user'''

import sys
import requests

if __name__ == '__main__':
    try:
        data = {'q', sys.argv[1]}
        with requests.post('http://0.0.0.0:5000/search_user', data). as req:
            print(req.text)
    except IndexError:
        print('No result')
    
