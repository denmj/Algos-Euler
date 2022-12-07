from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        ans = 0
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans

class SolutionTwoPointer:
    def trap(self, height: List[int]) -> int:
        
        pass
        
        # if not height:
        #     return 0
        # n = len(height)
        # left, right = 0, n - 1
        # left_max, right_max = height[0], height[n - 1]
        # ans = 0
        # while left < right:
        #     left_max = max(left_max, height[left])
        #     right_max = max(right_max, height[right])
        #     if left_max < right_max:
        #         ans += left_max - height[left]
        #         left += 1
        #     else:
        #         ans += right_max - height[right]
        #         right -= 1
        # return ans

# height = [0,1,0,2,1,0,1,3,2,1,2,1]






       # if not height:
        #     return 0
        # n = len(height)
        # left_max = [0] * n
        # right_max = [0] * n
        # left_max[0] = height[0]
        # right_max[n - 1] = height[n - 1]
        # for i in range(1, n):
        #     left_max[i] = max(left_max[i - 1], height[i])
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(right_max[i + 1], height[i])
        # ans = 0
        # for i in range(n):
        #     ans += min(left_max[i], right_max[i]) - height[i]
        # return ans
