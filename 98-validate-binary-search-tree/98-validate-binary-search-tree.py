# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(tree, leftBound, rightBound):
            if not tree:
                return True
            
            if not (tree.val < rightBound and tree.val > leftBound):
                return False
            
            
            return dfs(tree.left, leftBound, tree.val) and dfs(tree.right, tree.val, rightBound)
        
        return dfs(root, float('-inf'), float('inf'))
        