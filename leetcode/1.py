from typing import List

# hashMap solution 
class SolutionHashMap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):
            n = target - num
            if n not in hmap:
                hmap[num] = i
            else:
                return [hmap[n], i]

# Brute force solution
class SolutionBrute:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 167 is the same as 1, but the array is sorted