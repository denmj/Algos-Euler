from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_count = len(words)
        word_len = len(words[0])
        window_size = word_count * word_len
        ans = []
        for i in range(len(s)-window_size+1):
            if self.is_valid(s[i:i+window_size], words):
                ans.append(i)
        return ans


# test 
