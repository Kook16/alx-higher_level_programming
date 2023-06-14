#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    sum = 0
    for item in set(my_list):
        sum += item
    return sum
