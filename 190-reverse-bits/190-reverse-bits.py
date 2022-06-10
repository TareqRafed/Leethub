class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        
        for i in range(32):
            currentBit = (n >> i) & 1
            res |= currentBit << (31 - i)
        
        return res