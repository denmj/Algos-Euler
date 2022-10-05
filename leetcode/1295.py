from typing import List, Optional

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = [1 for i in nums if len(str(i)) % 2 == 0]
        return sum(count)
