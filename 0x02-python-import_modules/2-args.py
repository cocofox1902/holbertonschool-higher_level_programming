#!/usr/bin/python3
import sys
nb = len(sys.argv)

if nb == 1:
    print("0 arguments.")
elif nb == 2:
    print("1 argument:")
else:
    print("{} arguments:".format(nb - 1))
for i in range(1, nb):
    print("{}: {}".format(i, sys.argv[i]))
