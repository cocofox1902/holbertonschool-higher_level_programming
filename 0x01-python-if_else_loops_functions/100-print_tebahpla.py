#!/usr/bin/env python3
for c in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{}".format(c, chr(c - 33)), end="")
