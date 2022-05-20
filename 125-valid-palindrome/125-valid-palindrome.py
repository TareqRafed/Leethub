class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s.lower()
        fixed = ''.join(filter(str.isalnum, s)).lower()
        
        
        l, r = 0, len(fixed) - 1
        
        print(fixed)
        isP = True
        while l <= r:
            if fixed[l] != fixed[r]:
                isP = False
                break
            l += 1
            r -= 1
        
        return isP