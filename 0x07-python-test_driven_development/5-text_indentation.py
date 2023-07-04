#!/usr/bin/python3
'''
Defining text_indentation function
'''


def text_indentation(text):
    '''
    text_identation - prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text: A string repesenting the message
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    split_text = text.split()
    seperator = ['.', '?', ':']
    i = len(split_text)
    k = 0
    for item in split_text:
        for s in seperator:
            if s in item:
                print(item)
                print()
                break
        else:
            if k is not i - 1:
                print(item, end=' ')
            else:
                print(item, end='')
        k += 1
