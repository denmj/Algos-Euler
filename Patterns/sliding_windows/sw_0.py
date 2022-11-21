import math 


# one way
def average_subarray_v0(arr: list, k: int) -> list:
    average_list = []
    average = 0
    for indx in range(len(arr)-(k-1)):
        for num in arr[indx:indx+k]:
            average = average + num
        average_list.append(average/k)
        average = 0
    return average_list

# complexity O(n*k)
# Average of sliding window - second way
def average_subarray_v1(arr: list, k: int) -> list:
    return [sum(arr[i:i+k]) / k for i in range(len(arr)-(k-1))]

# Test case for average_subarray
# L = [1, 3, 2, 6, -1, 4, 1, 8, 2]


# complexitu O(n)
def average_subarray_v2(arr: list, k: int) -> list:
    pass
    # Keep intermediate sum of current window
    # subtract first element of previous window and add last element of current window
    # return average
    

# no set use
def diff_substring_v0(s: str, k: int) -> int:
    ans = 0
    temp_set = []
    for i in range(len(s)-(k-1)):
        for c in s[i:i+k]:
            if c not in temp_set:
                temp_set.append(c)
        if len(temp_set) == k:
            ans += 1
        temp_set = []
    return ans


def diff_substring(s: str, k: int) -> int:
    ans = 0
    for i in range(len(s)-(k-1)):
        if len(set(s[i:i+k])) == k:
            ans += 1
    return ans

# Test case for diff_substring
# s = "xyzzaz" # 1
# s = "aababcabc" # 2