#!/usr/bin/python3
"""module to add arguments"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argc = len(sys.argv)

try:
    file = load_from_json_file("add_item.json")
except:
    file = []

if argc >= 2:
    for lenght in range(1, argc):
        file.append(sys.argv[lenght])

save_to_json_file(file, "add_item.json")
