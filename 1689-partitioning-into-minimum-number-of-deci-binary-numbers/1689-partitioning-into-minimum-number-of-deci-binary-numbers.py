class Solution:
    def minPartitions(self, n: str) -> int:
        
        ans = 0
        
        for val in n:
            
            ans = max(ans, int(val))
            if ans == 9:
                return ans
        
        return ans