# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot):
            
            if not root:
                if not subRoot:
                    return True
                return False
            
            if not subRoot and root:
                return False
            
            if root.val == subRoot.val:
                return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
            
            return False
        
        roots = [root]
        
        while roots:
            val = roots.pop()
            if val:
                if val.val == subRoot.val:
                    if dfs(val, subRoot):
                        return True
                roots.append(val.left)
                roots.append(val.right)
        
        return False
        