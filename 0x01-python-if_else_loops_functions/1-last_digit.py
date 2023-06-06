#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    signed_number = number * -1
    last_digit = -1 * (signed_number % 10)
else:
    unsigned_number = number
    last_digit = unsigned_number % 10
if last_digit > 5:
    message = 'and is greater than 5'
elif last_digit < 6 and last_digit != 0:
    message = 'and is less than 6 and not 0'
elif last_digit == 0:
    message = 'and is 0'
print(f"Last digit of {number} is {last_digit} {message}")
