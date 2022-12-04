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

# (E)
def removeDuplicates(nums: List[int]) -> int:
    left, right = 0, 1

    while right < len(nums):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
        right += 1
    return left + 1

# test_arr = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4]

# (M)
def removeDups(nums: List[int]) -> int:
    left, right = 0, 1
    count = 1
    while right < len(nums):
        if nums[left] == nums[right]:
            count += 1
        else:
            count = 1
        if count <= 2:
            left += 1
            nums[left] = nums[right]
        right += 1


    return left + 1


sorted_sq = [-11, -10, -7, -5, -2]

def sortedSquared(nums: List[int]) -> List[int]:
    # left, right = 0, len(nums) - 1
    mid, n = 0, len(nums)
    for i in range(n):
        if nums[i] >= 0:
            mid = i
            break

    print(mid)
    # left, right = mid - 1, mid
    # result = []
    # while left >= 0 and right < n:
    #     if nums[left] ** 2 < nums[right] ** 2:
    #         result.append(nums[left] ** 2)
    #         left -= 1
    #     else:
    #         result.append(nums[right] ** 2)
    #         right += 1
    # while left >= 0:
    #     result.append(nums[left] ** 2)
    #     left -= 1
    # while right < n:
    #     result.append(nums[right] ** 2)
    #     right += 1
    # return result


def maxArea(height: List[int]) -> int:
    
    
    pass
    
    # left, right = 0, len(height) - 1
    # max_area = 0
    # while left < right:
    #     max_area = max(max_area, min(height[left], height[right]) * (right - left))
    #     if height[left] < height[right]:
    #         left += 1
    #     else:
    #         right -= 1
    # return max_area

N = [1, 8, 6, 2, 5, 4, 8, 3, 7]
left, right = 0, len(N) - 1
max_area = 0

while left < right:
    print(left, right)
    left += 1
    right -= 1

print(min(5, 4*2))

def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area