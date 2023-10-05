#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    element = 0

    for i in my_list:
        try:
            print(i, end='')
            element += 1

            if element == x:
                break
        except Exception:
            pass

    print()
    return element
