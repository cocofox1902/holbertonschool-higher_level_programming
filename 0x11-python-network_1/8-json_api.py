#!/usr/bin/python3
""" 8 - json_api.py """


if __name__ == "__main__":
    import requests
    import sys

    q = "" if len(sys.argv) == 1 else sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        resp = r.json()
        if resp == {}:
            print('No result')
        else:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
    except ValueError:
        print('Not a valid JSON')
