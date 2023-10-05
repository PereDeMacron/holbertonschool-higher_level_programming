#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{}".format(my_list[i]), end=" " if count == 0 else " ")
                count += 1
        except IndexError:
            break
    print()
    return count
