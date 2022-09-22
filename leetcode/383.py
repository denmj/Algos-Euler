"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
"""

str1 = "aaa"
str2 = "aab"


class Solution:
    @staticmethod
    def canConstruct(ransomNote, magazine):
        """Given two strings ransomNote and magazine"""
        ransomNote_list = list(ransomNote)
        magazine_list = list(magazine)

        for i in ransomNote_list:
            if i in magazine_list:
                magazine_list.remove(i)
            else:
                return False
        return True


solution = Solution()
print(solution.canConstruct(str1, str2))