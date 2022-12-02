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

class SolutionPT:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            elif s < target:
                left += 1
            else:
                right -= 1