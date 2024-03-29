""""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


def sumOfPrimes(n):
    # list to store prime numbers
    prime = [True] * (n + 1)

    # Create a boolean array "prime[0..n]"
    # and initialize all entries it as true.
    # A value in prime[i] will finally be
    # false if i is Not a prime, else true.

    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then
        # it is a prime
        if prime[p] == True:
            # Update all multiples of p
            i = p * 2
            while i <= n:
                prime[i] = False
                i += p
        p += 1

        # Return sum of primes generated through
    # Sieve.
    sum = 0
    for i in range(2, n + 1):
        if (prime[i]):
            sum += i
    return sum

print(sumOfPrimes(2000000))