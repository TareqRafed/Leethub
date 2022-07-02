# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        val = []
        
        def dfs(root):
            if root:
                val.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        dfs(root) 
        return ' '.join(val)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        preorder = list(map(int, data.split()))
        inorder = sorted(preorder)
        ans = self.build(preorder, inorder)
        return ans
    
    def build(self, preorder, inorder):
        # build a tree from preorder and inorder
        if not preorder or not inorder:
            return
        mid = preorder[0]
        root = TreeNode(mid)
        
        pre_index = inorder.index(mid)
        
        root.left = self.build(preorder[1:pre_index + 1], inorder[: pre_index])
        root.right = self.build(preorder[pre_index + 1:], inorder[pre_index + 1:])
        
        return root
        
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans