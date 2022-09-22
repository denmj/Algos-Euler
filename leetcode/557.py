

class Solution:
    @staticmethod
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in "Let's take LeetCode contest".split()])


solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
