#!/usr/bin/python3
import py_compile
import hidden_4

if __name__ == "__main__":
    module_attributes = dir(hidden_4)

    for attr in sorted(module_attributes):
        if not attr.startswith('__'):
            print(attr)
