class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        ###
        # 1 -> 2
        # 2 -> 1, 3
        # 3 -> 4, 2
        # 4 -> 3
        ###

        graph = defaultdict(list)

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
        
        stack = [root]
        ans = []
        visited = set()
        visited.add(root)

        while stack:
            node = stack.pop()
            ans.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)
            graph[node] = []
        
        return ans