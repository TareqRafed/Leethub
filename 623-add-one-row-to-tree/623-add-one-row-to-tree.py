# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root, None)
        
        def bfs():
            curr = deque([(root, 1)])
            while curr:
                node = curr.popleft()
                if not node[0]:
                    continue
                if node[1] == depth - 1:
                    node[0].left = TreeNode(val, node[0].left, None)
                    node[0].right = TreeNode(val, None, node[0].right)
                curr.append((node[0].left, node[1] + 1))
                curr.append((node[0].right, node[1] + 1))
                
                
                    
        bfs()
        return root