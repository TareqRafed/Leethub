class Solution:
    def longestPalindrome(self, s: str) -> str:
        anw = ''
        start = 0
        end = 0
        
        
        def expandCenter(first, last):
            l, r = first, last
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #print(s[l], s[r])
                l -= 1
                r += 1
            l+= 1
            
            return s[l:r]
        
        for i in range(len(s)):
            len1 = expandCenter(i, i+1)
            len2 = expandCenter(i, i)
            #print('test', len1, len2)
            maxSum = max(len(len1), len(len2))
            if maxSum > len(anw):
                anw = len1 if len(len1) == maxSum else len2
        
        
        
        return anw