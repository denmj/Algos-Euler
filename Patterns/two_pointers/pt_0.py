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

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 7

def TwoSums(nums: List, target: int) -> List:

    left, right = 0, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

def moveZeros(nums: List[int]) -> List[int]:
    left, right = 0, 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

        right += 1
    return nums
 
#  l = [0, 1, 0, 3, 12]
