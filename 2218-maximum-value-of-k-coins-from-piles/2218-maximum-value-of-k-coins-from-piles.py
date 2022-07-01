class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        
        @lru_cache(None)
        def dp(index, n):
            
            if index == len(piles) or n == 0: return 0
            
            res = dp(index + 1, n)
            curr = 0
            
            for j in range(min(len(piles[index]), n)):
                curr += piles[index][j]
                res = max(res, curr + dp(index + 1, n-j-1))
            return res 
        
        return dp(0, k)
    

