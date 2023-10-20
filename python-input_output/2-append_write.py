#!/usr/bin/python3
"""def a fonction that appends a string at the end of a text file
and returns the number of characters added"""
def append_write(filename="", text=""):
    """append a string to a text file and return the number of characters was add"""

    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
