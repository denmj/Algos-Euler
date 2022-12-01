from typing import List

class Solution:
    def TwoSums(nums: List, target: int) -> List:

        left, right = 0, len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]