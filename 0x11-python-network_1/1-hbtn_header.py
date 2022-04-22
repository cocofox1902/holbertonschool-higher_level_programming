#!/usr/bin/python3
""" 1 - hbtn_header.py """


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        html = response.headers.get('X-Request-Id')
        print(html)
