from typing import Any, Callable, Dict, List, Optional, Tuple, Union

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(set(nums))
