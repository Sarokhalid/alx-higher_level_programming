#!/usr/bin/python3
"""print list in sorted"""


class MyList(list):
    def print_sorted(self):
        """print list in sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
