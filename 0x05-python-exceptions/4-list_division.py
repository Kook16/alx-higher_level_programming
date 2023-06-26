#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is None or my_list_2 is None:
        print('out of range')
    result = 0
    list = []
    i = 0
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            return
        except ZeroDivisionError:
            print('division by 0')
            return
        except IndexError:
            print("out of range")
            return
        finally:
            list.append(result)
        i += 1
    return list
