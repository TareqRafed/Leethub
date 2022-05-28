# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        qu = collections.deque()
        qu.append(root)
        ans = []
        while qu:
            lenQ = len(qu)
            lvl = []
            for i in range(lenQ):
                node = qu.popleft()
                
                if node:
                    lvl.append(node.val)
                    qu.append(node.left)
                    qu.append(node.right)
            if lvl:
                ans.append(lvl)
            
        
        return ans