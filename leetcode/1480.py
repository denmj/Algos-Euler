"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(n, i) for i, n in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[0])

        left_side = 0
        right_side = len(nums) - 1
        while left_side < right_side:
            result = nums[left_side][0] + nums[right_side][0]
            if result == target:
                return [nums[left_side][1], nums[right_side][1]]
            elif result < target:
                left_side += 1
            else:
                right_side -= 1


s = Solution()
print(s.twoSum([5, 13, 7, 2, 11, 15], 9))
