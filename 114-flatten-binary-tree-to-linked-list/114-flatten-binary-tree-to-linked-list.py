# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        items = []
        def dfs(root):
            if not root:
                return
            items.append(root)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        if not items:
            return
        
        for i in range(1, len(items)):
            items[i - 1].right = items[i]
            items[i - 1].left = None
        
        items[-1].left = None
        items[-1].right = None