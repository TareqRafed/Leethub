# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def trev(root, sum):
            if not root:
                return False
            
            sum += root.val

            if sum == targetSum and root.left is None and root.right is None:
                return True
            
            return trev(root.left, sum) or trev(root.right, sum)
        return trev(root, 0)