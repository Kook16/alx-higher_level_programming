#!/usr/bin/python3
if __name__ == "__main__":
        import sys

argument = sys.argv[1:]
argument_num = len(argument)
index = 1
if argument_num == 1:
        print("{} argument:".format(argument_num))
elif argument_num < 1:
    print("{} arguments.".format(argument_num))
else:
    print("{} arguments:".format(argument_num))
for i in argument:
    print("{}: {}".format(index, i))
    index = index + 1
