# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0, True
            elif not root.left and not root.right:
                return 1, True
            else:
                l_h, l_b = dfs(root.left)
                r_h, r_b = dfs(root.right)
                is_b = True if abs(l_h-r_h) <= 1 else False
                return max(l_h, r_h) + 1, is_b and l_b and r_b
                
        # 1 l_h=1 r_h=3 - 4, False
        # 2 - 1
        # 3 l_h=2 r_h=0 - 3, False
        # 4 l_h=1 r_h=0 - 2, True
        # 5 - 1
        h, is_b = dfs(root)
        return is_b
