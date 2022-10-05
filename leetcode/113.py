from typing import List, Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root, p, r, targetSum):
        if not root:
            return

        p.append(root.val)

        if not root.left and not root.right and targetSum == root.val:
            r.append(list(p))

        self.dfs(root.left, p, r, targetSum - root.val)

        self.dfs(root.right, p, r, targetSum - root.val)

        p.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []
        self.dfs(root, [], ans, targetSum)
        return ans