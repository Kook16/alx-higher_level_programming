#!/usr/bin/python3
def safe_print_integer(value):
    if value is None:
        return
    try:
        print("{:d}".format(int(value)))
    except (ValueError, TypeError):
        return False
    return True
