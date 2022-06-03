# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_res = root.val
        
        def dfs(tree):
            nonlocal max_res
            if not tree:
                return 0
            
            max_left = max(dfs(tree.left), 0)
            max_right = max(dfs(tree.right), 0)
            
            max_res = max(max_res, tree.val + max_left + max_right)
            
            return tree.val + max(max_left, max_right)
            
            
        
        dfs(root)
        return max_res