# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        
        res = []
        def backtrack(start, end):
            
            if start > end:
                return [None]
            
            all_trees = []
            
            for i in range(start, end + 1):
                
                all_left_trees = backtrack(start, i - 1)

                all_right_trees = backtrack(i + 1, end)
                
                for l_tree in all_left_trees:
                    for r_tree in all_right_trees:
                        n_tree = TreeNode(i)
                        
                        n_tree.left = l_tree
                        n_tree.right = r_tree
                        
                        all_trees.append(n_tree)
            
            return all_trees
        
        return backtrack(1, n) if n > 0 else []
                        
            
            
            
            