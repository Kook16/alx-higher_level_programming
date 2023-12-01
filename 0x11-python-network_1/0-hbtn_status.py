#!/usr/bin/python3
'''
A script that
fetches https://intranet.hbtn.io/status.
'''
import urllib.request as r

if __name__ == '__main__':
    req = r.Request('https://alx-intranet.hbtn.io/status')

    with r.urlopen(req) as response:
        html = response.read()
        print('Body response:')
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        print(f'\t- utf8 content: {html.decode("utf-8")}')
