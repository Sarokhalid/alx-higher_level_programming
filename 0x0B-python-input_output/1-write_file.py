#!/usr/bin/python3
"""hgfgj"""


def write_file(filename="", text=""):
    """jggjkg"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
