#!/usr/bin/python3
for number in range(0, 100):


    if number < 99:
        if number < 10:
            number = '0' + str(number)
        print(f'{number},', end=' ')
    else:
        print(number)
