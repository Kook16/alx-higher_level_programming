#!/usr/bin/python3
'''Defining a write_file function
'''


def write_file(filename="", text=""):
    '''write_file - writes a string to a text file and return no of characters
    written
    Args:
         filename: name to file to write to
         text: This the string to be written to filename
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        bytes_written = file.write(text)
    return bytes_written
