class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hmap = defaultdict(list)
        visited = set()
        for crs, pre in prerequisites:
            hmap[crs].append(pre)
        
        def dfs(val):
            if val in visited:
                return False
            
            if hmap[val] == []:
                return True
            
            visited.add(val)
            #print(visited, val)
            
            for crs in hmap[val]:
                if not dfs(crs): return False
            
            
            visited.remove(val)
            hmap[val] = []
            return True
        
        
        for val in range(numCourses):
            if not dfs(val):
                return False
        
        return True