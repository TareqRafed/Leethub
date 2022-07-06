class Solution:
    def fib(self, n: int) -> int:
        
        @lru_cache(None)
        def tail_recurs(i, a, b):
            if i == 0:
                return a
            elif i == 1:
                return b
            else:
                return tail_recurs(i - 1, b, a + b)
            
        
        return tail_recurs(n, 0, 1)