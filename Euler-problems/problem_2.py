"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def problem_2(n):
    num_1 = 0
    num_2 = 1
    if n < 0:
        return -1
    elif n == 0:
        return num_1
    elif n == 1:
        return num_2
    else:
        sum = 0
        for i in range(2, n):

            num_3 = num_1 + num_2
            if num_3 % 2 == 0:
                sum += num_3
            print(num_3)
            num_1 = num_2
            num_2 = num_3
        return sum


print(problem_2(34))
