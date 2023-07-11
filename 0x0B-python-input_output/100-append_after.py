#!/usr/bin/python3
'''DEfining a append_after function
'''


def append_after(filename="", search_string="", new_string=""):
    '''this function inserts a line of text to a file, after each line
    containing a specific string
    '''
    text = ""
    with open(filename, encoding='utf-8') as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w', encoding='utf-8') as updated:
        updated.write(text)
