from typing import List, Optional
#
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1
        print(arr)


arr = [1, 0, 2, 3, 0, 4, 5, 0]

Solution().duplicateZeros(arr)
