#!/usr/bin/python3
"""
    Write a script that adds all arguments to a Python
    list, and then save them to a file
"""

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    from sys import argv
    json_file = "add_item.json"

    try:
        json_list = load_json(json_file)
    except:
        json_list = []
    for item in argv[1:]:
        json_list.append(item)
    save_json(json_list, json_file)
