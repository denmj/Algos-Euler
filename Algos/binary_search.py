# binary search in sorted array
import math

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = math.floor((low + high) / 2)
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search(sorted_list, 5))