"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

import numpy as np


def multiply(x, res, res_size):
    # Initialize carry
    carry = 0

    # One by one multiply n with
    # individual digits of res[]
    for i in range(res_size):
        prod = res[i] * x + carry

        # Store last digit of
        # 'prod' in res[]
        res[i] = prod % 10

        # Put rest in carry
        carry = prod // 10

    # Put carry in res and
    # increase result size
    while (carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size += 1

    return res_size

MAX = 100000

def power(x, n):


    res = [0 for i in range(MAX)]
    res_size = 0
    temp = x

    # Initialize result
    while (temp != 0):
        res[res_size] = temp % 10;
        res_size += 1
        temp = temp // 10

    # Multiply x n times
    # (x^n = x*x*x....n times)
    for i in range(2, n + 1):
        res_size = multiply(x, res, res_size)
    digit = []
    print(x, "^", n, " = ", end="")
    for i in range(res_size - 1, -1, -1):
        # print(res[i], end="")
        digit.append(res[i])
    return digit


exponent = 1000
base = 2
p = power(base, exponent)

print(np.sum(p))