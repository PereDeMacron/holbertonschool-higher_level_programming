#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Write the given text to a file and return the number of characters written.

    Args:
        filename: the name of the file to write in
        text: the text to write in the file.

    returns: the number of characters was write in the file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_characters_written = file.write(text)
        return num_characters_written
    except Exception as e:
        return 0

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
