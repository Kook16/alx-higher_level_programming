#!/usr/bin/python3
'''
Script that takes in a URL and an email, sends a POST request
 And displays the body of the response
'''

import urllib.request as r
import urllib.parse as p
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {
        'email': sys.argv[2]
        }

    data = p.urlencode(value)
    data = data.encode('ascii')
    req = r.Request(url, data)
    with r.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
