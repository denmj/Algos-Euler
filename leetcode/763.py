from typing import List

class SolutionHashMap:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = size = 0
        ans = []
        for i, c in enumerate(S):
            size += 1
            j = max(j, last[c])
            if i == j:
                ans.append(size)
                size = 0
        return ans

# st = 'ababcbacadefegdehijhklij'
