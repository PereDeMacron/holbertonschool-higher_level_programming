#!/usr/bin/python3
"""def a function for read and print a text file"""


def read_file(filename=""):
    """print in stdout the contents of a  text file in UTF8"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
