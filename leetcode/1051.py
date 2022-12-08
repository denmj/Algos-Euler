from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        p1, count = 0, 0
        while p1 < len(heights):
            if heights[p1] != sorted_heights[p1]:
                count += 1
            p1 += 1
        return count