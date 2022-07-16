class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        memo = {}
        
        def dfs(i, j, visited):
            key = (i, j)
            if key in memo and len(visited) == 0:
                return memo[key]
            
            
            
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
            
            count = 0
            
            count += dfs(i, j + 1, visited)
            count += dfs(i, j - 1, visited)
            count += dfs(i + 1, j, visited)
            count += dfs(i - 1, j, visited)
            
            memo[key] = count + 1
            return memo[key]
        
        
        
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, dfs(i, j, set()))
        
        return ans