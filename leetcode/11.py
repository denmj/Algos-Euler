from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right  = 0, len(height) - 1
        max_a = 0
        
        while left < right:
            max_a = max(max_a, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_a