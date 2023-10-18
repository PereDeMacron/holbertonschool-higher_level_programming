#!/usr/bin/python3
"""define a class list"""
class MyList(list):
    """define print list in ascendent sorted order"""
    def print_sorted(self):
        """print list in sorted order"""
        print(sorted(self))
