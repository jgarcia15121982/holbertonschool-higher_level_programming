#!/usr/bin/python3
"""Script that adds all arguments to a Python list
   and then save them to a file"""

import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file('add_item.json')
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, 'add_item.json')
except FileNotFoundError:
    save_to_json_file(sys.argv[1:], 'add_item.json')
