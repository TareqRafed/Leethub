# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([(root, 1)])
        hmap = {
            1: root.val,
        }
        while queue:
            node, level = queue.popleft()
            
            if node:
                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))
                if node.right and not level + 1 in hmap:
                    hmap[level + 1] = node.right.val
                elif node.left and not level + 1 in hmap:
                    hmap[level + 1] = node.left.val
        
        return list(hmap.values())