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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7

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
    


print(TwoSums(numbers, target))



# p1, p2 = 0, len(numbers)-1

# while p1 < p2:
#     sum = numbers[p1] + numbers[p2]
#     print("Index of : ", p1, "for: ", numbers[p1])
#     print("Index of : ", p2, "for: ", numbers[p2])
#     print("Sum of: ", numbers[p1], "and", numbers[p2], "is: ", sum)
#     p1 += 1 
#     p2 -= 1
