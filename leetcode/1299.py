from typing import List, Optional
import time

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, x in enumerate(arr):
            if arr[i + 1:]:
                arr[i] = max(arr[i + 1:])

        arr[-1] = -1

        return arr
