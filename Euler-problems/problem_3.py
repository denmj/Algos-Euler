"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def problem_3(num):
    max_prime = -1

    # Print the number of 2s that divide n
    while num % 2 == 0:
        max_prime = 2
        num >>= 1  # equivalent to n /= 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            max_prime = i
            num = num / i

    if num > 2:
        max_prime = num
    return int(max_prime)
