from typing import Any, Callable, Dict, List, Optional, Tuple, Union

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(set(nums))


class Solution_2:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1

        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
