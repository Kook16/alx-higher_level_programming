#!/usr/bin/python3
"""
 a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import requests.auth as r
import sys

if __name__ == '__main__':
    url = f'https://api.github.com/users/{sys.argv[1]}'
    req = requests.get(url,
                       auth=r.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))
