#!/usr/bin/python3
""" 7 - error_code.py """


if __name__ == "__main__":
    import requests
    import sys

    respond = requests.get(sys.argv[1])
    if respond.status_code >= 400:
        print("Error code: {}".format(respond.status_code))
    else:
        print(respond.text)
