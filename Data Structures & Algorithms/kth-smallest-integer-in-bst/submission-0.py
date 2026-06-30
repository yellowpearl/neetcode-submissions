# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, stack):
            if not root or len(stack) > k:
                return
            
            dfs(root.left, stack)
            stack.append(root.val)
            dfs(root.right, stack)

        stack = []
        dfs(root, stack)
        return stack[k-1]

