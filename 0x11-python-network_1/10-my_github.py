#!/usr/bin/python3
'''Takes your github credentials (username and password ) and
uses the Github API to display your id'''

# Usage: username password

import sys
import requests
from requests.auth import HTTPBasicAuth


auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
with requests.get('https://api.github.com/user', auth=auth) as req:
    print(req.json().get('id'))
