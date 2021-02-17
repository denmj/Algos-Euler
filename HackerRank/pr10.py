
"""
Task
You are given a polynomial  of a single indeterminate (or variable),
You are also given the values of x and k Your task is to verify if P(x) = k

"""

integer_list = list(map(int, input().split()))

poly = input()
x = integer_list[0]
k = integer_list[1]

print(eval(poly) == k)
