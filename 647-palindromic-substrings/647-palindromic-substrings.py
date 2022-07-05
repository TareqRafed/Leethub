class Solution:
    
    def calculatePalindrom(self, i, j, s):
        counter = 0
        while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
            j += 1
            i -= 1
            counter += 1
        return counter
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        
        for i in range(0, len(s)):
            if i - 1 >= 0 and s[i - 1] == s[i]:
                ans += self.calculatePalindrom(i - 1, i, s)
            if i - 1 >= 0 and i + 1 <= len(s) - 1 and s[i - 1] == s[i + 1]:
                ans += self.calculatePalindrom(i - 1, i + 1, s)
        return ans

    