# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        def treeToArray(pre, ino):
            #print(pre, ino)
            if not pre or not ino:
                return None
            
            mid_val = pre[0]
            pre_index = ino.index(mid_val)
            
            root = TreeNode(mid_val)
            
            root.left = treeToArray(pre[1:pre_index + 1], ino[:pre_index])
            root.right = treeToArray(pre[pre_index + 1:], ino[pre_index + 1:])
            #print(root)  
            return root
            
        
        return treeToArray(preorder, inorder)