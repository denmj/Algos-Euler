from typing import List


class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        """Given two strings s and t, determine if they are isomorphic."""
        index_of_s = {}
        index_id_s = []
        index_of_t = {}
        index_id_t = []
        for i, c in enumerate(s):
            if c not in index_of_s:
                index_of_s[c] = i
            index_id_s.append(str(index_of_s[c]))

        for i1, c1 in enumerate(t):
            if c1 not in index_of_t:
                index_of_t[c1] = i1
            index_id_t.append(str(index_of_t[c1]))
        s_id = ' '.join(index_id_s)
        t_id = ' '.join(index_id_t)

        print(index_of_s)
        print(index_id_t)

        print(s_id)
        print(t_id)
        return s_id == t_id


solution = Solution()
print(solution.isIsomorphic("egg", "add"))