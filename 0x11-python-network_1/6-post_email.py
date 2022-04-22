#!/usr/bin/python3
""" 6 - post_email.py """


if __name__ == "__main__":
    import requests
    import sys

    email = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(email.text)
