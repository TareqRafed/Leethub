class Solution:
    def reverse(self, x: int) -> int:
        
        if x.bit_length() > 32:
            return 0
        
        toStr = list(str(abs(x)))
        
        l, r = 0, len(toStr) -1 
        
        while l <= r:
            toStr[l], toStr[r] = toStr[r], toStr[l]
            l += 1
            r -= 1
        ans = int(''.join(toStr))
        print(ans.bit_length())
        if ans.bit_length() >= 32:
            return 0
        if x < 0:
            return ans * -1
        return ans