"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


# Brute force solution


def nth_prime(num):
    n = 2
    prime_counter = 0
    num_of_prime = num
    while prime_counter < num_of_prime:
        # Check from 2 to n-1
        for i in range(2, n):
            if (n % i == 0):
                break
        else:
            prime_counter += 1
        n += 1
    print(n-1)


nth_prime(10001)
