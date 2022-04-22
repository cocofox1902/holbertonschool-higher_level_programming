#!/usr/bin/python3
""" 10 - my_github.py """


if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get('https://api.github.com/user',
                        auth=(sys.argv[1], sys.argv[2]))
    if resp.status_code >= 400:
        print('None')
    else:
        print(resp.json().get('id'))
