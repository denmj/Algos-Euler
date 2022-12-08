# (E)
from typing import List

class Solution:
    def sortArrayByParityBrute1(self, A: List[int]) -> List[int]:
        # Brute
        odd = []
        even = []

        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        return even + odd

    def sortArrayByParityBrute2(self, A: List[int]) -> List[int]:

        return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 != 0])

    def sortArrayByParityTwoPointer(self, A: List[int]) -> List[int]:

        # Two pointer odd and even
        left, right = 0, 0

        while right < len(A):
            if A[right] % 2 == 0:
                A[left], A[right] = A[right], A[left]
                left += 1

            right += 1

        return A

T = [3,1,2,4]
s= Solution()
s.sortArrayByParityTwoPointer(A=T)