# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = defaultdict(list)
        def bfs(root, rootSib, lvl = 0):
            if not root and not rootSib:
                return
            
            if root and not rootSib:
                ans[lvl].append(root.val)
                bfs(root.left, root.right, lvl + 1)
                return
            
            if rootSib and not root:
                ans[lvl].append(rootSib.val)
                bfs(rootSib.left, rootSib.right, lvl + 1)
                return
            
            ans[lvl].append(root.val)
            ans[lvl].append(rootSib.val)
            
            bfs(root.left, root.right, lvl + 1)
            bfs(rootSib.left, rootSib.right, lvl + 1)
            
            
            
            
        bfs(root, None)
        return ans.values()