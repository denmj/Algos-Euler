"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example,
 "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple,
 return the substring of the earliest occurrence. If there are none, return an empty string.
"""

#  alternates Upper and Lower case letters
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        for i in range(len(s)):
            if s[i].islower():
                if s[i].upper() not in s:
                    return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key=len)
            else:
                if s[i].lower() not in s:
                    return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key=len)
        return s



# Test case for longestNiceSubstring
s = "YazaAay"

print(Solution().longestNiceSubstring(s))

