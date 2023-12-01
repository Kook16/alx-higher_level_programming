#!/usr/bin/python3
'''A script that takes in a URL,
Sends a request to the URL,
And displays the value of the X-Request-Id
 variable found in the header ofthe response.
'''
import urllib.request as r
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = r.Request(url)

    with r.urlopen(req) as response:
        header = response.getheaders()
        header_dict = dict(header)
        if 'X-Request-Id' in header_dict:
            print(header_dict['X-Request-Id'])
