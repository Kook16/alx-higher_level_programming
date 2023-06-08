#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = sys.argv[1:]
    total = 0
    for x in argument:
        x = int(x)
        total += x
    print(total)
