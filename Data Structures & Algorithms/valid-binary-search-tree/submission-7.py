# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, min_val, max_val):
            if not curr:
                return True
            
            if (min_val is not None and curr.val <= min_val) or (max_val is not None and curr.val >= max_val):
                return False
            
            return dfs(curr.left, min_val, curr.val) and dfs(curr.right, curr.val, max_val)
        return dfs(root, None, None)



