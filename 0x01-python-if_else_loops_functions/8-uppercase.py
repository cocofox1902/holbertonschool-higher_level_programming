#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            charactere = chr(ord(i) - 32)
        else:
            charactere = i
        print("{}".format(charactere), end="")
    print('')
