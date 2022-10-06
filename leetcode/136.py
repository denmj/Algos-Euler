from typing import List, Optional

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass


nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
nums2 = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6]
nums3 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]


def singleNumber(nums: List[int]) -> int:
    nums.sort()

    for i in range(0, len(nums), 2):
        print(i, i+1, len(nums))
        if i + 1 == len(nums):
            return nums[i]
        if nums[i] != nums[i + 1]:
            return nums[i]

print(singleNumber(nums3))
