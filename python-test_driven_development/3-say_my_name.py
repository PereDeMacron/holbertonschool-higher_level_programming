#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = "My name is "
    if last_name:
        full_name += first_name + " " + last_name
    else:
        full_name += first_name

    print(full_name)
