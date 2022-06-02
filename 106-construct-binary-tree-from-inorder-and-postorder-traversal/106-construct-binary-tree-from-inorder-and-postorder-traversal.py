# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        def arrayToTree(ino, post):
            
            if not ino or not post:
                return None
            
            root_val = post[-1]
            mid_index = ino.index(root_val)
            
            root = TreeNode(root_val)
            
            root.right = arrayToTree(ino[mid_index + 1:], post[mid_index:-1])
            root.left = arrayToTree(ino[:mid_index], post[0:mid_index])
            
            return root
        
        return arrayToTree(inorder, postorder)
            