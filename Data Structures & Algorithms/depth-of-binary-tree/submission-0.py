# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = deque()
        c = 0
        if root:
            d.append(root)
        while d:
            for i in range(len(d)):
                curr = d.popleft()
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            c += 1
        return c
        