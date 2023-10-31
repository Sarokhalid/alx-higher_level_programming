#!/usr/bin/python3
def uppercase(string):
    for char in string:
        upp = chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char
        print("{}".format(upp), end="")
    print()
