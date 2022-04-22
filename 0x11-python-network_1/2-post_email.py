#!/usr/bin/python3
""" 2 - post_email.py """


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    email = {'email': argv[2]}
    value = urllib.parse.urlencode(email).encode('ascii')
    post = urllib.request.Request(argv[1], value)
    with urllib.request.urlopen(post) as response:
        print(response.read().decode('utf-8'))
