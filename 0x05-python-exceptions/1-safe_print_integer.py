#!/usr/bin/python3
def safe_print_integer(value):
    if value is None:
        return
    try:
        print("{:d}\n".format(value))
    except ValueError:
        return False
    return True
