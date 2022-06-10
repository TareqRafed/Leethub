class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        
        for i in range(32):
            currentBit = (n >> i) & 1
            
            if currentBit == 1:
                res += 1
        return res