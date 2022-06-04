"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        hmap = {}
        
        stack = [node]
        while stack:
            innerNode = stack.pop()
            if innerNode.val in hmap:
                continue
            
            hmap[innerNode.val] = Node(innerNode.val, [])
            
            for val in innerNode.neighbors:
                stack.append(val)
            
        
        stack = [node]
        while stack:
            innerNode = stack.pop()
            if len(innerNode.neighbors) == len(hmap[innerNode.val].neighbors):
                continue
            for val in innerNode.neighbors:
                hmap[innerNode.val].neighbors.append(hmap[val.val])
                stack.append(val)
        
        
        return hmap[node.val] 
            
        