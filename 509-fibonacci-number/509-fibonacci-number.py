class Solution:
    def fib(self, n: int) -> int:
        
        @lru_cache(None)
        def dfs(i):
            if i == 0 or i == 1:
                return i
            if i < 0:
                return 0
            
            return dfs(i - 1) + dfs(i - 2)
        
        return dfs(n)