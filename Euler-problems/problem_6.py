"""
The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def problem_6(num):
    sum_of_sq = 0
    sum = 0
    for n in range(1, num+1):
        sq = n * n
        sum_of_sq += sq
        sum += n
        sq_of_sum = sum * sum
        diff = sq_of_sum - sum_of_sq
    return sum_of_sq, sq_of_sum, diff





