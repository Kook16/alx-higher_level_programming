#!/usr/bin/python3
'''Defining a write_file function
'''


def append_write(filename="", text=""):
    '''append_write - appends a string at the end of a text file and
    return no of characters added
    Args:
         filename: name to file to write to
         text: This the string to be apended to filename
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        bytes_written = file.write(text)
    return bytes_written
