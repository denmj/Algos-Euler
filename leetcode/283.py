from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1


l_test = [0,1,0,3,12]
s = Solution()
s.moveZeros(nums= l_test)  