# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res = []
        def dfs(root, path, goal):
            if not root:
                return
            
            path.append(root)
            
            if root.val == goal:
                res.append(path.copy())
            
            
            dfs(root.left, path.copy(), goal)
            dfs(root.right, path.copy(), goal)
            
        
        dfs(root, [], p.val)
        dfs(root, [], q.val)
        
        p_p = res[0]
        q_p = res[1]
        
        for i in range(len(p_p) - 1, -1, -1):
            for j in range(len(q_p) - 1, -1, -1):
                if p_p[i] == q_p[j]:
                    return p_p[i]