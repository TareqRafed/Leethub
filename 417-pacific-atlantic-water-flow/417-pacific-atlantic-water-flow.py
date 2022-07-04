class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        
        a, p = set(), set()
        va, vp = set(), set()
        
        for r in range(m):
            a.add((r, n - 1))
            p.add((r, 0))
        
        for c in range(n):
            p.add((0, c))
            a.add((m - 1, c))
        
        dirc = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, visited):
            visited.add((r, c))
            
            for di, dj in dirc:
                n_r, n_c = r + di, c + dj
            
                if 0 <= n_r < m and 0 <= n_c < n and heights[r][c] <= heights[n_r][n_c] and (n_r, n_c) not in visited:
                    dfs(n_r, n_c, visited)
        
        for r, c in p:
            dfs(r, c, vp)
        
        for r, c in a:
            dfs(r, c, va)
        
        return vp & va
                    