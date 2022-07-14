# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        def buildTree(pre, ino):
            
            if not pre and not ino:
                return
            
            tree = TreeNode(pre[0])
            
            rootIno = ino.index(pre[0])
            
            
            tree.left = buildTree(pre[1:rootIno + 1], ino[:rootIno])
            tree.right = buildTree(pre[rootIno + 1:], ino[rootIno + 1:])
            
            return tree
        
        return buildTree(preorder, inorder)