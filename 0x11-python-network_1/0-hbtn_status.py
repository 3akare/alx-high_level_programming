#!/usr/bin/python3
'''Script that fetches https://alx-intranet.htbn.io/status'''


if __name__ == '__main__':
    import urllib.request

    text = '''Body response:\n\t- type: \
{}\n\t- content: {}\n\t- utf8 content: {}'''
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(text.format(type(result), result, str(result)[2:-1]))
