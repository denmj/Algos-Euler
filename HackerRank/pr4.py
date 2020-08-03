"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly
 four of the five integers.
 Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""

arr = [1, 2, 3, 4, 5]


def miniMaxSum(l):
    max_arr = l.copy()
    min_arr = l.copy()
    max_arr.remove(max(max_arr))
    min_arr.remove(min(min_arr))
    print(sum(max_arr), sum(min_arr))


miniMaxSum(arr)