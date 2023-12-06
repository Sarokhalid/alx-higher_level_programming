#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        """
        Print the list in ascending order (sorted).
        Note:
            This method assumes that all
            elements of the list are of type int
        """
        sorted_list = sorted(self)
        print(sorted_list)
