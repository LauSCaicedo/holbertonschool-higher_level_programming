#!/usr/bin/python3
'''
Script that adds all arguments
to a Python list, and then save
them to a file.
'''


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

l_fname = 'add_item.json'
''' List must be saved as a JSON
representation in a file named add_item.json.
'''
try:
    file_found = load_from_json_file(l_fname)
except FileNotFoundError:
    file_found = []
for i in argv[1:]:
    file_found.append(i)
save_to_json_file(file_found, l_fname)
