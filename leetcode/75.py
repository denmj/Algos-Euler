from typing import List

class SolutionTwoPointer:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        right = left
        while right < len(nums):
            if nums[right] == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1