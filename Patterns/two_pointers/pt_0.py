from typing import List
# Palindrome (E)

# s = "racecar"
# s2 = "race a car"
# s3 = 'A man, a plan, a canal: Panama'

def is_palindrome(s: str) -> bool: 
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

# (M)

numbers = [11, 23, 2, 5, 7, 11, 15]
target = 7

def TwoSums(nums: List, target: int) -> List:


    nums = sorted(nums)
    left, right = 0, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []
    






p1, p2 = 0, len(numbers)-1

while p1 < p2:
    print("Index of : ", p1, "for: ", numbers[p1])
    print("Index of : ", p2, "for: ", numbers[p2])
    print("Sum of: ", numbers[p1], "and", numbers[p2], "is: ", numbers[p1] + numbers[p2])
    p1 += 1 
    p2 -= 1
