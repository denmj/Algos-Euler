from typing import List

grid = [[7, 1, 3], [2, 8, 7], [1, 9, 5]]


class Solution:
    @staticmethod
    def maximumWealth(accounts: List[List[int]]) -> int:
        max_account = 0
        for account in accounts:
            if sum(account) > max_account:
                max_account = sum(account)
        return max_account


solution = Solution()
print(solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))