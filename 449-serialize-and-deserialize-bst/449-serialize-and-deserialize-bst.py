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
        def b(stop):
            if inorder and inorder[-1] != stop: ## check if first element in inorder (before reversing) is not reached yet
                root = TreeNode(preorder.pop()) # get the root by getting first element of preorder
                root.left = b(root.val)
                inorder.pop()
                root.right = b(stop)
                return root
            
        ## to get pop left with O(n) complexity
        preorder.reverse()
        inorder.reverse()
        return b(None)
        
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans