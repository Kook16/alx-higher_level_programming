#!/usr/bin/python3
'''Defining a read_file function
'''


def read_file(filename=""):
    '''This function reads a text file(UTF*) and printd iy out to stdout
    Args:
        filename: Name of the file to read from, by default its an empty string
    '''
    try:
        with open(filename, encoding='UTF8') as file:
            file_read = file.read()
    except FileNotFoundError:
        pass
    else:
        print(file_read)
