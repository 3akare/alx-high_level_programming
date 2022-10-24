#!/usr/bin/python3
''' Add all arguments to a python list, and then save them to a file'''
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    new_list = load_from_json_file('add_item.json')
except Exception:
    new_list = []

for i in range(len(sys.argv)):
    if i != 0:
        new_list.append(sys.argv[i])

save_to_json_file(new_list, 'add_item.json')
