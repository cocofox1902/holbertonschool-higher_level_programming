#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
print("Last digit of ", end="")
if number < 0:
    ld = -ld
if ld > 5:
    print("{} is {} and is greater than 5".format(number, ld))
elif ld == 0:
    print("{} is {} and is 0".format(number, ld))
elif 6 > ld != 0:
    print("{} is {} and is less than 6 and not 0".format(number, ld))
