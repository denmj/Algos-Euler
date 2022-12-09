from typing import List

class Solution:
    def findDisappearedNumbersBrute(self, nums: List[int]) -> List[int]:
        # O(n) time and O(1) space

        n_min, n_max = 1, len(nums)
        res = []
        for i in range(1, len(nums)+1):
            print(i)
            if i not in nums:
                res.append(i) 
        
        return res

    def findDisappearedNumbersOn(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
