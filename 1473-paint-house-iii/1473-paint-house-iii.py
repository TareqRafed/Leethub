class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        ans = 0
        
        @lru_cache(None)
        def dfs(i, nc, pc):
            if i == len(houses) and nc == target:
                return 0
            
            if i >= len(houses) and nc != target:
                return float('inf')
            
            if houses[i] != 0:
                return dfs(i + 1, nc + (pc != houses[i]), houses[i])
            
            return min(dfs(i + 1, nc + (pc != clr), clr) + cost[i][clr-1] for clr in range(1, n+1))
        
        ans = dfs(0, 0, 0)
        return ans if ans != float('inf') else -1