#!/usr/bin/python3
def safe_print_integer(value):
    if value is None:
        return False
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
