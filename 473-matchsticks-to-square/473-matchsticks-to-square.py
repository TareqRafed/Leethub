class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        allSum = sum(matchsticks)
        
        edge = allSum / 4
        
        if edge < max(matchsticks) or allSum % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        
        @cache
        def bt(l1, l2, l3, l4, i):
            nonlocal edge
            if l1 == l2 == l3 == l4 == edge:
                return True
            
            if i >= len(matchsticks):
                return False
            
            if edge < l1 or edge < l2 or edge < l3 or edge < l4:
                return False
            
            return (
                bt(l1 + matchsticks[i], l2, l3, l4, i + 1) or 
                bt(l1, l2 + matchsticks[i], l3, l4, i + 1) or
                bt(l1, l2, l3 + matchsticks[i], l4, i + 1) or
                bt(l1, l2, l3, l4 + matchsticks[i], i + 1)
            )
            
        
        
        
        
        return bt(0, 0, 0, 0, 0)
        