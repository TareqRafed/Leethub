class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        
        
        count = {}
        
        ans, l, r = 0, 0, 0
        c = k
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            
            mostFreq = (None, 0)
            # get max freq in count
            for key, value in count.items():
                if value > mostFreq[1]:
                    mostFreq = (key, value)
            
            if s[r] != mostFreq[0]:
                c -= 1
            
            while (r - l) + 1 > mostFreq[1] + k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, (r - l) + 1)
            r += 1
        
        return ans