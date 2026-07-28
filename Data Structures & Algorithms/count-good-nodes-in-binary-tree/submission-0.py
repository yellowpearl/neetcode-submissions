# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, m):
            if not curr:
                return 0
            
            c = 0
            if curr.val >= m:
                c += 1
            m = max(m, curr.val)
            return c + dfs(curr.left, m) + dfs(curr.right, m)
        return dfs(root, float('-inf'))