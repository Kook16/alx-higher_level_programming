#!/usr/bin/python3
'''Defining a read_file function
'''


def read_file(filename=""):
    '''This function reads a text file(UTF*) and printd iy out to stdout
    Args:
        filename: Name of the file to read from, by default its an empty string
    '''
    with open(filename, encoding='utf-8') as file:
        file_read = file.read()
        print(file_read, end="")
