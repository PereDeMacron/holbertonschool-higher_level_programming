#!/usr/bin/python3

"""
This module provides a function for writing text to a file and returning the number of characters written.

The main function in this module is 'write_file', which allows you to specify a filename and the text to write to the file. It returns the number of characters written to the file.

Usage:
    To use this module, call the 'write_file' function with the desired filename and text to write. The function will create or overwrite the file with the given text and return the character count. In case of any errors, it returns 0.

Example:
    from your_module import write_file

    # Write text to a file and get the character count
    character_count = write_file("my_file.txt", "Hello, World!\n")
    print(f"Characters written: {character_count}")
"""

def write_file(filename="", text=""):
    """
    Write the given text to a file and return the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file. Returns 0 in case of an error.

    Raises:
        Exception: If an error occurs while writing to the file.

    Note:
        Make sure the 'filename' argument contains a valid path to the file, and the 'text' argument is a string.
"""

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
