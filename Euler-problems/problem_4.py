"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91×99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(s):
    if s is not str:
        s = str(s)
    if s == s[::-1]:
        return int(s)
    else:
        return -1


def problem_4():
    palin_numer = 0
    for num1 in range(1, 100):
        for num2 in range(1, 100):
            sum = num1 * num2
            palin_num = palindrome(sum)
            if (palin_num > 1):
                palin_numer = palin_num
    return palin_numer




