#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return
    i = 0
    count = 0
    while i < x:
        try:
            flag = 1
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            flag = 0
        except IndexError:
            break
        if flag:
            count += 1
        i += 1
    print()
    return count
