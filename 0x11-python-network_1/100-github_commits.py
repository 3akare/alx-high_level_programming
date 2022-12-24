#!/usr/bin/python3
'''A script that takes 2 arguments in order to solve this challenge'''
# print out the last 10 commits of a repository


import sys
import requests

if __name__ == '__main__':
    URL = 'https://api.github.com/repos/{}/{}/commits'
    with requests.get(URL.format(sys.argv[1], sys.argv[2])) as response:
        req = response.json()
        for i in range(0, 10):
            name = req[i].get('sha')
            sha = req[i].get('commit').get('author').get('name')
            print('{}: {}'.format(name, sha))
