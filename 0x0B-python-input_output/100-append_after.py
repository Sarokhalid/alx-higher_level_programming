#!/usr/bin/python3
"""fhkkkgf"""


def append_after(filename="", search_string="", new_string=""):
    """dhjk"""
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filename, mode='w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
