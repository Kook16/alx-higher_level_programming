#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            message = "FizzBuzz"
        elif number % 3 == 0:
            message = "Fizz"
        elif number % 5 == 0:
            message = "Buzz"
        else:
            message = chr(number)
        print(f'{message} ')
