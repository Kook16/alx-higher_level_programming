#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    average = 0
    sum = 1
    i = 0
    total = 0
    for item in my_list:
        for item1 in item:
           sum *= item1
           i += item1
        total += sum
