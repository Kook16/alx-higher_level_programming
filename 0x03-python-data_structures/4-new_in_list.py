#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list_copy = my_list[:]
    if my_list is None:
        return
    elif idx < 0 or idx > len(my_list) -1:
        return my_list
    else:
        my_list_copy[idx] = element
        return my_list_copy
