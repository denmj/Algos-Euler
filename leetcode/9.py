class Solution:
    def isPalindrome(self, x: int) -> bool:
        srt_x = str(x)
        return srt_x == srt_x[::-1]
