#!/usr/bin/python3
if __name__ == "__main__":
        from calculator_1 import add, sub, mul, div

a = 10
b = 5
add_add = add(a, b)
sub_sub = sub(a, b)
mul_mul = mul(a, b)
div_div = div(a, b)
print("{} + {} = {}".format(a, b, add_add))
print("{} - {} = {}".format(a, b, sub_sub))
print("{} * {} = {}".format(a, b, mul_mul))
print("{} / {} = {}".format(a, b, div_div))
