#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None:
        return
    max_int = my_list[0]
    if len(my_list) == 0:
        return None
    for item in my_list:
        if item > max_int:
            max_int = item
    return max_int
