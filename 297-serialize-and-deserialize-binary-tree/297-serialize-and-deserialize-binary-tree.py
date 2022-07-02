# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = ''
        def dfs(root):
            nonlocal string
            if root:
                string += f'{root.val},'
                dfs(root.left)
                dfs(root.right)
            else:
                string += 'null,'
        dfs(root) 
        return string
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        #print(data)
        
        data = data.split(',')
        data.pop()
        i = 0
        def dfs():
            nonlocal i
            if data[i] == 'null':
                i += 1
                return
            
            root = TreeNode()
            root.val = data[i]
            
            i += 1
            root.left = dfs()
            root.right = dfs()
            
            return root

        return dfs()
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))