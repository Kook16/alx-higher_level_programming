#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = []
    for item in my_list:
        new_list.append(item)
    for item in new_list[:]:
        if item == search:
            new_list[new_list.index(search)] = replace
    return new_list
