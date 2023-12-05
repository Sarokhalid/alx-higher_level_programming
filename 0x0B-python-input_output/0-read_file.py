#!/usr/bin/python3
"""class"""


def read_file(filename=""):
    """read file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
