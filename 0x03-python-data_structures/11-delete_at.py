#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx > len(my_list) - 1 or idx  < 0:
        return my_list
    else:
        i = 0
        while i < len(my_list):
            if my_list[i] == my_list[idx]:
                break
            i += 1
        my_list.remove(my_list[i])
        return my_list
