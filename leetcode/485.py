from typing import List, Optional


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        max_ = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if count > max_:
                max_ = count
        return max_


solution = Solution()
print(solution.findMaxConsecutiveOnes(nums=[1,1,0,1,1,1,0,0,1,1,1,1,1,1,1]))















        # max_ = 0
        # count = 0
        # for i in nums:
        #     if i == 1:
        #         count += 1
        #     else:
        #         count = 0
        #     if count > max_:
        #         max_ = count
        # return max_