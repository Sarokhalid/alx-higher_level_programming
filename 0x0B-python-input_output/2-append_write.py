#!/usr/bin/python3
"""fhjjj"""


def append_write(filename="", text=""):
    """hjjjff"""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
