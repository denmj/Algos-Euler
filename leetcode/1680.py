from typing import List, Optional


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        concat_binary = "".join([bin(x).replace("0b", "") for x in range(1, n+1)])

        return int(concat_binary, 2) % mod


solution = Solution()
print(solution.concatenatedBinary(n=12))


# x_ = "".join([bin(x).replace("0b", "") for x in range(1, 5+1)])
