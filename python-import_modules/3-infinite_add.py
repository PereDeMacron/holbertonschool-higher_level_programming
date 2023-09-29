#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        result = 0
    else:
        result = sum(int(arg) for arg in args)

    print(result)
