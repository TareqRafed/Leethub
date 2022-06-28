class Solution:
    def minDeletions(self, s: str) -> int:
        word = sorted(s)
        co = Counter(word) 
        vis = set()
        res = 0
        for key in co.keys():
            val = co[key]
            while val in vis and val > 0:
                res += 1
                val -= 1
            if val != 0:
                vis.add(val)
        
        return res
            
        
        